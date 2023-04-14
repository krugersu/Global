
import time
import sys
import json
import shutil
import sendFile
from datetime import datetime
from types import SimpleNamespace
from pathlib import Path  
import diff_data
import logging
import m_config
from datetime import datetime
from pprint import pprint

#import MySQLdb
import pymysql
#import m_config
import codecs

#import app_logger

import settings
import logging.config

if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    import pysqlite3
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
   import sqlite3


#logger = app_logger.get_logger(__name__)
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger('my_logger')






class workDb:
    def __init__(self,rc, c_count = None):
        
        self.pathDB = Path("/home/administrator/Global/data", "myDB.sqlite")
        #print(Path("data", "myDB.sqlite"))
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                pysqlite3.paramstyle = 'named'
                self._all_db = pysqlite3.connect(self.pathDB)
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            sqlite3.paramstyle = 'named'
            self._all_db = sqlite3.connect(self.pathDB)
        logger.info('Connect DB')    
        self.sale_dict = []
        
        logger.info('Start create DB')    
        self.pathScript = Path("/home/administrator/Global/data", "createDB.sql") 
        self._cursor = self._all_db.cursor()
        self.baseTableName = 'invent'
        
        self.c_count = c_count
        
        self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
            database=rc._sections.artix.database,
            user=rc._sections.artix.user,
            passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor() #cursor created
        logger.info('Connect to MySql DB')    
        
    def __enter__(self):
        
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        
        self.close()
        
    @property
    def connection(self):
        
        return self._conn
    
    @property
    def cursor(self):
        
        return self._cursor
    
    def commit(self):
        self.connection.commit()
    def close(self, commit=True):
        if commit:
            self.commit()
        self.connection.close()
    def execute(self, sql, params=None):
        self.cursor.execute(sql, params or ())
    def fetchall(self):
        return self.cursor.fetchall()
    def fetchone(self):
        return self.cursor.fetchone()
    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()

    def querySales(self):
        # Запрос в БД Артикс по текущим продажам
        #executing the query
        # self._mycursor.execute(diff_data.qrSimpleSelectSale)
        for  value in self.sale_dict:    # 
            #for k, v in value.items():
                print(value['cashcode'])
                print(value['shiftnum'])
                logger.info('cashcode - ' + str(value['cashcode']))    
                logger.info('shiftnum - ' + str(value['shiftnum']))    
                # self._mycursor.execute(diff_data.qrGetNumWorkshift,(value['shiftnum']),)
                # num_workshift = self._mycursor.fetchone() 
                #print('num_workshift '+ str(num_workshift))
                
                self._mycursor.execute(diff_data.qrSimpleSelectSale,(value['cashcode'],(value['shiftnum'])),)

                x = []
                rows = self._mycursor.fetchall()
                logger.info('rows - ' + str(rows))    
        #showing the rows
                for row in rows:
                    x.append(row)
                self._cursor.executemany('INSERT INTO goodsitem VALUES(?,?,?)',x)    
                self._all_db.commit() 
        self.mydb.close()

        
    def createDB(self):
        """AI is creating summary for createDB
        """        
        with open(self.pathScript, 'r') as sql_file:
            sql_script = sql_file.read()

        self.cursor.executescript(sql_script)
        self._all_db.commit()

    
    
    def uploadData(self,c_count, shop_Number):
                
        self.createDB()
        logger.debug('Function call - recursive_items(c_count)' )
        self.recursive_items(c_count)
        logger.debug('Function call - calculating_the_amount()' )
        self.calculating_the_amount()
        logger.debug('Function call - delete_analog()' )
        self.delete_analog()
        logger.debug('Function call - delete_null_parent()' )
        self.delete_null_parent()
        logger.debug('Function call - querySales()' )
        self.querySales()
        logger.debug('Function call - calculateSales()' )
        self.calculateSales()
        logger.debug('Function call - ctest_db(shop_Number)' )
        self.test_db(shop_Number)
        
    def recursive_items(self,dictionary):
        # Берем данные из УНФ т записываем в соответствующие таблицы БД для последующей обработки
        logger.info('Start add DB from 1C')
        count = 0
        #for item in dictionary.invent:
        #    pprint(item)
        self._cursor.executemany(diff_data.qrAddinvent, dictionary.invent,)
        count = count + len(dictionary.invent)
      #  pprint(dictionary.additionalprices)
        self._cursor.executemany(diff_data.qrAddadditionalprices, dictionary.additionalprices,)    
        count = count + len(dictionary.additionalprices)
        self._cursor.executemany(diff_data.qrAddBarcodes, dictionary.barcodes,)
        count = count + len(dictionary.barcodes)
        self._cursor.executemany(diff_data.qrAddinventitemoptions, dictionary.inventitemoptions,)        
        count = count + len(dictionary.inventitemoptions)
        self._cursor.executemany(diff_data.qrAddPriceoptions, dictionary.priceoptions,)                    
        count = count + len(dictionary.priceoptions)
        self._cursor.executemany(diff_data.qrAddquantityoptions, dictionary.quantityoptions,)                    
        count = count + len(dictionary.quantityoptions)
        self._cursor.executemany(diff_data.qrAddSellrestrictperiods, dictionary.sellrestrictperiods,) 
        count = count + len(dictionary.sellrestrictperiods)
        self._cursor.execute(diff_data.qrAddOptions)
        self._all_db.commit()                                
        
        # Текущие закрытые кассовые смены по данному обрабатываемому магазину 
        self.sale_dict = dictionary.wsunf
       # pprint(dictionary.wsunf)
        #pprint(self.sale_dict)
        
        
        logger.info('workshift from UNF - ' + str(dictionary.wsunf))    
        logger.info('End add DB from UNF')    
        logger.info('added - ' + str(count) + ' records')    


    def calculating_the_amount(self):
        """Запускает SQL скрипт, который переносит количество с аналагов пива на головную номенклатуру"""        
        pathScript = Path("/home/administrator/Global/data", "upd.sql") 
        #pprint(Path("data", "upd.sql"))
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
            #print(sql_script)
        self._cursor.executescript(sql_script)
        logger.info('Summ analog calcalating')  
        
    def delete_analog(self):
        """Запускает SQL скрипт, который удаляет из базы аналоги после перенесения количества на головную"""        
        pathScript = Path("/home/administrator/Global/data", "del_a.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        self._all_db.commit()
        logger.info('Delete analog')  
        
    def delete_null_parent(self):
        """Запускает SQL скрипт, который удаляет из базы головную номенклатуру с нулевым количеством, т.е. которая пришла из 1С, но
            на неё не было распределения"""        
        pathScript = Path("/home/administrator/Global/data", "del_null_count_parent.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        self._all_db.commit()
        logger.info('Delete 0 parent count')      

        
    def calculateSales(self):
        """Запускает SQL скрипт, который отнимает проданное от пришедшего товара"""        
        pathScript = Path("/home/administrator/Global/data", "updateprod.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        logger.info('Sales calcalating')              
        
        
    def test_db(self,shop_Number):
        """Maps a number from one range to another.
    :param number:  The input number to map.
    :param in_min:  The minimum value of an input number.
    :param in_max:  The maximum value of an input number.
    :param out_min: The minimum value of an output number.
    :param out_max: The maximum value of an output number.
    :return: The mapped number.
    """
        
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                self._all_db.row_factory = pysqlite3.Row # Позволяет работать с возвращаемым результатам с обращением к столбцам по имени
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            self._all_db.row_factory = sqlite3.Row
        
        #outfile = open('tData.aif', 'w',encoding='utf-8')  
        curFileName = 'pos' + str(shop_Number) + '.aif'
        curFlagName = 'pos' + str(shop_Number) + '.flz'
        
        pathAif = Path("/home/administrator/Global/upload/", curFileName) 
        pathFlz = Path("/home/administrator/Global/upload/", curFlagName) 
        
        outfileFlz = open(pathFlz, 'w',encoding='utf-8')  
        outfileFlz.close
        #outfile = open(pathAif, 'w',encoding='utf-8')  
        with open(pathAif, 'w',encoding='utf-8') as outfile:
        
            outfile.writelines(diff_data.header+ '\n')
            outfile.writelines(json.dumps(diff_data.clearInventory)+ '\n')
        
            outfile.writelines(diff_data.separator+ '\n')
            outfile.writelines(json.dumps(diff_data.clearTmcScale)+ '\n')    
            outfile.writelines(diff_data.separator+ '\n')
        
            dictForArtix = {}
            c = self._all_db.cursor()
        
            c.execute('SELECT * FROM invent')                          
            
            while True:
                invent=c.fetchone()
                if invent:

            # Add Barcodes
                    cBar = self._all_db.cursor()
    #                nDict = dict(diff_data.addInventItem) 
    #                tCommand = diff_data.addInventItem      
                    
                    nDict = (dict(invent))
    #               nCommand = {}
    #              tCommand.update(nDict)
                    
                    tCode = ((nDict['inventcode']))


                    cBar.execute(diff_data.qrBarcodes,(tCode,))
                                            
                    tBarcodes = dict(invent)
                    barcodes = cBar.fetchall()  
                    allBarcodes = []
                    for itm in barcodes:
                        allBarcodes.append((dict(itm)) )
                    
                    #nDict['barcodes'] = allBarcodes
                    
                    # Add sellrestrictperiods Массив ограничений продаж по времени, пока не заполняем, нам без надобности
                    cSellPeriod = self._all_db.cursor()       
                    cSellPeriod.execute(diff_data.qrsellrestrictperiods,(tCode,))
                    sellrestrictperiods = cSellPeriod.fetchall()  
                    allSellrestrictperiods = []
                    for itm in sellrestrictperiods:
                        allSellrestrictperiods.append((dict(itm)) )


                    # Add Additionalprices  Массив дополнительных цен
                    cAdditionalprices = self._all_db.cursor()       
                    cAdditionalprices.execute(diff_data.qrAdditionalprices,(tCode,))
                    additionalpricesid = cAdditionalprices.fetchall()  
                    alladditionalpricesid = []
                    for itm in additionalpricesid:
                        alladditionalpricesid.append((dict(itm)) )



                    # Add inventitemoptions Опции товара
                    cinventitemoptions = self._all_db.cursor()       
                    cinventitemoptions.execute(diff_data.qrinventitemoptions,(tCode,))
                    inventitemoptions = cinventitemoptions.fetchall()  
                    # allinventitemoptions = {}
                    for itm in inventitemoptions:
                        # allinventitemoptions.append((dict(itm)) )
                        allinventitemoptions = (dict(itm))

                    # Add priceoptions Опции цены
                    cpriceoptions = self._all_db.cursor()       
                    cpriceoptions.execute(diff_data.qrpriceoptions,(tCode,))
                    priceoptions = cpriceoptions.fetchall()  
                    # allpriceoptions = []
                    for itm in priceoptions:
                        allpriceoptions = (dict(itm)) 
            


                    # Add quantityoptions Опции количества
                    cquantityoptions = self._all_db.cursor()       
                    cquantityoptions.execute(diff_data.qrquantityoptions,(tCode,))
                    quantityoptions = cquantityoptions.fetchall()  
                    #allquantityoptions = []
                    for itm in quantityoptions:
                        allquantityoptions = (dict(itm))



                    # Add quantityoptions Опции количества
                    cremainsoptions = self._all_db.cursor()       
                    cremainsoptions.execute(diff_data.qrremainsoptions,(tCode,))
                    remainsoptions = cremainsoptions.fetchall()  
                    #allremainsoptions = []
                    for itm in remainsoptions:
                        allremainsoptions = (dict(itm))

            
    ##########################################################################################
                    # Add options Опции товара
                    '''   coptions = self._all_db.cursor()       
                    coptions.execute("SELECT * FROM options where optionsidid = ?",(tCode,))
                    options = coptions.fetchall()   '''
                    alloptions = {}
                    alloptions['inventitemoptions'] = allinventitemoptions
                    alloptions['priceoptions'] = allpriceoptions
                    alloptions['quantityoptions'] = allquantityoptions   
                    #alloptions['remainsoptions'] = allremainsoptions   Опции учета остатков, пока ни как не реализованы, оставлены на будущее          
                    
                    ''' for itm in options:
                        alloptions.append((dict(itm)) ) '''
    ###########################################################################################



                        
                    nDict['options'] = alloptions                        
                    nDict['sellrestrictperiods'] = allSellrestrictperiods                    
                    nDict['additionalprices'] = alladditionalpricesid                    
                    nDict['barcodes'] = allBarcodes
                    
                    tCommand = diff_data.addInventItem      
                    comDict = (dict(tCommand))
                    nCommand = {}
                    nCommand['invent'] = nDict
                    comDict.update(nCommand)
                    
                    
                    #pprint(nDict)
                    
                    dictForArtix.update(comDict)

                    json.dump(dictForArtix, outfile,  indent=2,  ensure_ascii=False )
                    
                    outfile.write('\n' + diff_data.separator + '\n')    
                else:
                    break    
                
            
            outfile.writelines(diff_data.separator+ '\n')
            outfile.writelines(json.dumps(diff_data.clearAspectValueSet)+ '\n')    
            outfile.writelines(diff_data.separator+ '\n')
            
            
            outfile.write(diff_data.footer)  
#        outfile.close
        sendFile.sendFile(pathAif,shop_Number,True)
        sendFile.sendFile(pathFlz,shop_Number,False)
        
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!    
    def get_workshiftid(self,l_workshift):
        # Формируем список номеров открытых кассовых смен для добавление в БД
        l_wsh = []
        for row in l_workshift:
#            print(row[4])
            l_wsh.append(row[4])
        print(l_wsh)
        self.add_open_workshift(l_wsh)
        
    def add_open_workshift(self,l_workshift):
        # Добавляем открытые смены в БД
            #self._mycursor.execute(diff_data.qrAdd_workshift_open, [l_workshift])
            for wh in l_workshift:
                print('open - ' + str(wh))
                self._cursor.execute(diff_data.qrAdd_workshift_open, [str(wh),])
            self._all_db.commit()
        
    def get_close_workshift(self):
        
        saveworkshift_open = self._all_db.cursor() 
        # Список открытых смен из БД      
        saveworkshift_open.execute(diff_data.qrGet_saveworkshift_open)
        saveworkshift_open = saveworkshift_open.fetchall()  
        l_saveworkshift_open = []
        for itm in saveworkshift_open:
            print('for close_workshift - ' + str(itm))
            l_saveworkshift_open.append(str(itm[0]))
        print('Номера открытых смен из БД - ')
        print( l_saveworkshift_open)
        return l_saveworkshift_open
        
        
    def del_close_workshift(self,l_workshift):
        saveworkshift_del = self._all_db.cursor()       
        for wh in l_workshift:
            print('delete - ' + str(wh[5]))
            saveworkshift_del.execute(diff_data.qrDel_workshift_close,[str(wh[5])])
        self._all_db.commit()
        
    def close_db_connection(self):
        self._mycursor.close()
        self.mydb.close()
        logger.info('DB is closed!!!')    
        # def recursive_items(self,dictionary):
            
        # logging.info('Start add DB from 1C')
        # count = 0
        # for key  in dictionary:
        #     self.addRecord(dictionary[key],key)
        #     count = count + len(dictionary[key])
        
        # logging.info('End add DB from 1C')    
        # logging.info('added - ' + str(count) + ' records')    