
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
        # ???????????? ?? ???? ???????????? ???? ?????????????? ????????????????
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
        # ?????????? ???????????? ???? ?????? ?? ???????????????????? ?? ?????????????????????????????? ?????????????? ???? ?????? ?????????????????????? ??????????????????
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
        
        # ?????????????? ???????????????? ???????????????? ?????????? ???? ?????????????? ?????????????????????????????? ???????????????? 
        self.sale_dict = dictionary.wsunf
       # pprint(dictionary.wsunf)
        #pprint(self.sale_dict)
        
        
        logger.info('workshift from UNF - ' + str(dictionary.wsunf))    
        logger.info('End add DB from UNF')    
        logger.info('added - ' + str(count) + ' records')    


    def calculating_the_amount(self):
        """?????????????????? SQL ????????????, ?????????????? ?????????????????? ???????????????????? ?? ???????????????? ???????? ???? ???????????????? ????????????????????????"""        
        pathScript = Path("/home/administrator/Global/data", "upd.sql") 
        #pprint(Path("data", "upd.sql"))
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
            #print(sql_script)
        self._cursor.executescript(sql_script)
        logger.info('Summ analog calcalating')  
        
    def delete_analog(self):
        """?????????????????? SQL ????????????, ?????????????? ?????????????? ???? ???????? ?????????????? ?????????? ?????????????????????? ???????????????????? ???? ????????????????"""        
        pathScript = Path("/home/administrator/Global/data", "del_a.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        self._all_db.commit()
        logger.info('Delete analog')  
        
    def delete_null_parent(self):
        """?????????????????? SQL ????????????, ?????????????? ?????????????? ???? ???????? ???????????????? ???????????????????????? ?? ?????????????? ??????????????????????, ??.??. ?????????????? ???????????? ???? 1??, ????
            ???? ?????? ???? ???????? ??????????????????????????"""        
        pathScript = Path("/home/administrator/Global/data", "del_null_count_parent.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        self._all_db.commit()
        logger.info('Delete 0 parent count')      

        
    def calculateSales(self):
        """?????????????????? SQL ????????????, ?????????????? ???????????????? ?????????????????? ???? ???????????????????? ????????????"""        
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
                self._all_db.row_factory = pysqlite3.Row # ?????????????????? ???????????????? ?? ???????????????????????? ?????????????????????? ?? ???????????????????? ?? ???????????????? ???? ??????????
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
                    
                    # Add sellrestrictperiods ???????????? ?????????????????????? ???????????? ???? ??????????????, ???????? ???? ??????????????????, ?????? ?????? ????????????????????
                    cSellPeriod = self._all_db.cursor()       
                    cSellPeriod.execute(diff_data.qrsellrestrictperiods,(tCode,))
                    sellrestrictperiods = cSellPeriod.fetchall()  
                    allSellrestrictperiods = []
                    for itm in sellrestrictperiods:
                        allSellrestrictperiods.append((dict(itm)) )


                    # Add Additionalprices  ???????????? ???????????????????????????? ??????
                    cAdditionalprices = self._all_db.cursor()       
                    cAdditionalprices.execute(diff_data.qrAdditionalprices,(tCode,))
                    additionalpricesid = cAdditionalprices.fetchall()  
                    alladditionalpricesid = []
                    for itm in additionalpricesid:
                        alladditionalpricesid.append((dict(itm)) )



                    # Add inventitemoptions ?????????? ????????????
                    cinventitemoptions = self._all_db.cursor()       
                    cinventitemoptions.execute(diff_data.qrinventitemoptions,(tCode,))
                    inventitemoptions = cinventitemoptions.fetchall()  
                    # allinventitemoptions = {}
                    for itm in inventitemoptions:
                        # allinventitemoptions.append((dict(itm)) )
                        allinventitemoptions = (dict(itm))

                    # Add priceoptions ?????????? ????????
                    cpriceoptions = self._all_db.cursor()       
                    cpriceoptions.execute(diff_data.qrpriceoptions,(tCode,))
                    priceoptions = cpriceoptions.fetchall()  
                    # allpriceoptions = []
                    for itm in priceoptions:
                        allpriceoptions = (dict(itm)) 
            


                    # Add quantityoptions ?????????? ????????????????????
                    cquantityoptions = self._all_db.cursor()       
                    cquantityoptions.execute(diff_data.qrquantityoptions,(tCode,))
                    quantityoptions = cquantityoptions.fetchall()  
                    #allquantityoptions = []
                    for itm in quantityoptions:
                        allquantityoptions = (dict(itm))



                    # Add quantityoptions ?????????? ????????????????????
                    cremainsoptions = self._all_db.cursor()       
                    cremainsoptions.execute(diff_data.qrremainsoptions,(tCode,))
                    remainsoptions = cremainsoptions.fetchall()  
                    #allremainsoptions = []
                    for itm in remainsoptions:
                        allremainsoptions = (dict(itm))

            
    ##########################################################################################
                    # Add options ?????????? ????????????
                    '''   coptions = self._all_db.cursor()       
                    coptions.execute("SELECT * FROM options where optionsidid = ?",(tCode,))
                    options = coptions.fetchall()   '''
                    alloptions = {}
                    alloptions['inventitemoptions'] = allinventitemoptions
                    alloptions['priceoptions'] = allpriceoptions
                    alloptions['quantityoptions'] = allquantityoptions   
                    #alloptions['remainsoptions'] = allremainsoptions   ?????????? ?????????? ????????????????, ???????? ???? ?????? ???? ??????????????????????, ?????????????????? ???? ??????????????          
                    
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