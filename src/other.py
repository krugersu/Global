

#!/usr/bin/env python3.11


import os
import pathlib
from pathlib import Path



mPath = "E:\\unf_teleport\\26\\"

mPath.replace('\\\\', '//')

mPath = pathlib.PureWindowsPath(mPath)
#print(os.path.basename(mPath))
print(Path(mPath).parts[-1])



   #create_aif.saveTestFile()
   #c_count = request.send_request(c_shop,str(server_ip),str(port))
   # print(c_shop)
   
   #pathDB = Path("data", "myDB.sqlite") 
   #dbWork = workDB.Database(pathDB)


  print(rc.get('artix','server_ip'))
    r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
    r.encoding = 'utf-8' 
    print(r.status_code)
    #print(r.json())    
    #print(r.text)    




    '''  for item in dict_json.items():
        # item — это кортеж (ключ, значение)
        print(item[0]) '''
    #iterate(dict_json)   
   # tableName = []
#    tableName = getTableName(dict_json,tableName)
#    iterate(dict_json)
 #   textQuery = createQuery(tableName) 
   # createTable(textQuery)
    #createFullDB(dict_json)
       
    # data = json.load(json_file)


# Parse JSON into an object with attributes corresponding to dict keys.
    #x = json.loads(data, object_hook=lambda d: SimpleNamespace(**d))
  #  print(dict_json['invent']['price'],dict_json['invent']['options']['quantityoptions']['documentquantlimit'])
    
'''    with open('D:\Artix\Artix_gen\src\st.json', encoding='utf-8-sig') as json_file:
        json_data = json.loads(json_file.read())
    
    #Aim of this block is to get the list of the columns in the JSON file.
        columns = []
        column = []
        for data in json_data:
            column = list(data.keys())
            for col in column:
                if col not in columns:
                    columns.append(col)
                                
    #Here we get values of the columns in the JSON file in the right order.   
        value = []
        values = [] 
        for data in json_data:
            for i in columns:
                value.append(str(dict(data).get(i)))   
            values.append(list(value)) 
            value.clear()
        
    #Time to generate the create and insert queries and apply it to the sqlite3 database       
        create_query = "create table if not exists myTable ({0})".format(" text,".join(columns))
        insert_query = "insert into myTable ({0}) values (?{1})".format(",".join(columns), ",?" * (len(columns)-1))    
        print("insert has started at " + str(datetime.now()))  
        c = db.cursor()   
        c.execute(create_query)
        c.executemany(insert_query , values)
        values.clear()
        db.commit()
        c.close()
        print("insert has completed at " + str(datetime.now()))  '''
        
        
        
        #recursive function to iterate a nested dictionary      
''' def iterate(dictionary, indent=4):
  #  print('{')
    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
         #   print('1 '*indent, key, ": ", end='')
            iterate(value, indent+4)
        else:
            
            print('2 '*indent, key, ": ", value)
            
   # print(' '*(indent-4), '}') '''
    
''' def getTableName(dictionary,tableName, indent=1):

    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
            tableName.append(str(key))
            getTableName(value, tableName,indent)
        else:
            pass
   # print(tableName)
    return tableName


def createTable(textQuery):

    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 
     '''

''' def createQuery(tableName): 

    for table in tableName:
        users = table
        userid = table + 'id'
        textQuery =  f"""CREATE TABLE IF NOT EXISTS {users}( {userid} INT PRIMARY KEY );"""
        textQueryDelete =  f"""DROP TABLE IF EXISTS {users};"""
        deleteRecordTable(textQueryDelete)
        createTable(textQuery)
       # print (textQuery)
        
def createQueryColumn(tableName,colName): 

    textQuery =  f"""ALTER TABLE {tableName} ADD COLUMN {colName} 'TEXT'"""
    addColumn(textQuery)


def addColumn(textQuery):
    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 

def deleteRecordTable(textQuery):
    
    cur = all_db.cursor()
    cur.execute(textQuery)
    all_db.commit() 
    
    
# Попытка создать структуру БД при одном проходе структуры JSON    
def createFullDB(dictionary, indent=4):
    mTableName = ''
    for key, value in dictionary.items():
        #recurse if the value is a dictionary
        if type(value) is dict:
            mTableName = key
            #print(mTableName)
            print('1 '*indent, key, ": ", end='')
         #   createQuery(key)
         #   createFullDB(value, indent+4)
        else:
            #print(key)
          #  createQueryColumn(mTableName,key) 
            print('2 '*indent, key, ": ", value)
            


def saveDataDB(data):
    pass '''
    
    
    
'''     jtopy=json.dumps(data) #json.dumps take a dictionary as input and returns a string as output.
    dict_json=json.loads(jtopy)
 '''


''' def recursive_itemsD(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, dict):
        
            yield (key, value)
            yield from recursive_items(value)
        else:
            yield (key, value)

 '''    
 
         '''   
        if len (item_position['priceoptions']) > 0:
            curVal = diff_data.getListPriceoptions(item_position)
            self._cursor.execute(diff_data.qrAddPriceoptions,curVal) '''
    
        ''' if len (item_position['options']['quantityoptions']) > 0:
            curVal.clear()
            curVal = diff_data.getListquantityoptions(item_position)
            self._cursor.execute(diff_data.qrAddquantityoptions,curVal)
    
        if len (item_position['additionalprices']) > 0:
            curVal.clear()
            curVal = diff_data.getListadditionalprices(item_position)
            self._cursor.execute(diff_data.qrAddadditionalprices,curVal)
    
        if len (item_position['options']['inventitemoptions']) > 0:
            curVal.clear()
            curVal = diff_data.getListinventitemoptions(item_position)
            self._cursor.execute(diff_data.qrAddinventitemoptions,curVal)    
    
            curVal.clear()
            curVal = diff_data.getListinvent(item_position)
            self._cursor.execute(diff_data.qrAddinvent,curVal)     '''
    
    
    
    
    ''' def getListPriceoptions(item_position):
    
    curVal =[]
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['enablepricemanual'])) 
    curVal.append(int(item_position['requirepricemanual'])) 
    curVal.append(int(item_position['requireselectprice'])) 
    curVal.append(int(item_position['requiredeferredprice'])) 
    curVal.append(int(item_position['enableexcisemarkprice'])) 
    
    return curVal


def getListadditionalprices(item_position):
    
    curVal =[]
    
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['additionalprices']['pricecode'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    curVal.append(int(item_position['additionalprices']['price'])) 
    
    return curVal


def getListquantityoptions(item_position):
    
    curVal =[]
    
    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['options']['quantityoptions']['enabledefaultquantity'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitylimit'])) 
    curVal.append(int(item_position['options']['quantityoptions']['quantitylimit'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantityscales'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitybarcode']))     
    curVal.append(int(item_position['options']['quantityoptions']['enablequantitymanual'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantitymanual'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantitybarcode'])) 
    curVal.append(int(item_position['options']['quantityoptions']['requirequantityscales'])) 
    curVal.append(int(item_position['options']['quantityoptions']['enabledocumentquantitylimit']))     
    curVal.append(int(item_position['options']['quantityoptions']['autogetquantityfromscales'])) 
    curVal.append((item_position['options']['quantityoptions']['documentquantlimit']))     
    
    return curVal

def getListinventitemoptions(item_position):
    
    curVal =[]

    curVal.append(item_position['inventcode'].strip())
    curVal.append(int(item_position['options']['inventitemoptions']['disablebackinsale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventshow'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventsale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['disableinventback'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['requiredepartmentmanual']))     
    curVal.append(int(item_position['options']['inventitemoptions']['enabledepartmentmanual'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['enablebarcodemanual'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['enablebarcodescanner'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['visualverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['ageverify']))     
    curVal.append(int(item_position['options']['inventitemoptions']['requiresalerestrict'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['egaisverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['prepackaged'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['nopdfegaisverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['alcoset']))     
    curVal.append(int(item_position['options']['inventitemoptions']['freesale'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['rfidverify'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['lowweight'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['weightcontrolbypass'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['tobacco']))     
    curVal.append(int(item_position['options']['inventitemoptions']['shoes'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['fuzzyweight'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['ignoremarking'])) 
    curVal.append(int(item_position['options']['inventitemoptions']['markdownverify'])) 
    
    return curVal


def getListinvent(item_position):
    
    curVal =[]

    curVal.append(None) 
    curVal.append(item_position['inventcode'].strip()) 
    curVal.append(item_position['inventgroup']) 
    curVal.append(item_position['name']) 
    curVal.append(item_position['barcode'])
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['price']) 
    curVal.append(item_position['minprice']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['inventcode']) 
    curVal.append(item_position['extendedoptions']) 
    curVal.append(item_position['discautoscheme']) 
    curVal.append(item_position['deptcode']) 
    curVal.append(item_position['taxgroupcode']) 
    curVal.append(item_position['measurecode']) 
    curVal.append(item_position['remain']) 
    curVal.append(item_position['remaindate']) 
    curVal.append(item_position['articul']) 
    curVal.append(item_position['defaultquantity']) 
    curVal.append(item_position['taramode']) 
    curVal.append(item_position['taracapacity']) 
    curVal.append(item_position['aspectschemecode']) 
    curVal.append(item_position['aspectvaluesetcode']) 
    curVal.append(item_position['aspectusecase']) 
    curVal.append(item_position['aspectselectionrule']) 
    curVal.append(item_position['age']) 
    curVal.append(item_position['alcoholpercent']) 
    curVal.append(item_position['cquant']) 
    curVal.append(item_position['inn']) 
    curVal.append(item_position['kpp']) 
    curVal.append(item_position['alctypecode']) 
    curVal.append(item_position['paymentobject'])                   
    curVal.append(item_position['manufacturercountrycode']) 
    curVal.append(item_position['opmode']) 
    curVal.append(item_position['loyaltymode']) 
    curVal.append(item_position['minretailprice']) 
    curVal.append(item_position['Parent']) 
    curVal.append(item_position['isParent'].strip())                                                                                                                                                                                                                                           
    
    return curVal '''
    
    
    
    
    #pathDB = Path("data", "myDB.sqlite") 
#pathScript = Path("data", "createDB.sql") 

#all_db=sqlite3.connect(pathDB)
#all_db=pysqlite3.connect(pathDB)
#baseTableName = 'invent'


#server connection
''' mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd=""
)

  '''



''' c.execute('''WITH RECURSIVE parents AS (select * from invent
                    inner JOIN (SELECT *  FROM barcodes) as st
                    ON st.barcodesid  = invent.inventcode
                    )
                    SELECT *
                    FROM parents''') '''
                    
                    
                    
                            ''' while True:
            next_row = self._cursor.fetchone()
            if next_row:
                print(next_row)
            else:
                break '''
                
                
                
                
                *********************************************************
                
                
                

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


if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
    import pysqlite3
elif sys.platform == "darwin":
    pass
elif sys.platform == "win32":
   import sqlite3


class workDb:
    def __init__(self,rc, c_count = None):
        
        self.pathDB = Path("data", "myDB.sqlite")
        
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                pysqlite3.paramstyle = 'named'
                self._all_db = pysqlite3.connect(self.pathDB)
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            sqlite3.paramstyle = 'named'
            self._all_db = sqlite3.connect(self.pathDB)
        

        self.pathScript = Path("data", "createDB.sql") 
        self._cursor = self._all_db.cursor()
        self.baseTableName = 'invent'
        
        self.c_count = c_count
        
        self.mydb = pymysql.connect(host=rc._sections.artix.server_ip,
            database=rc._sections.artix.database,
            user=rc._sections.artix.user,
            passwd=rc._sections.artix.passwd)
        self._mycursor = self.mydb.cursor() #cursor created

        
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

        #executing the query
        self._mycursor.execute(diff_data.qrSimpleSelectSale)

        x = []
        rows = self._mycursor.fetchall()
        #rows = self._mycursor.fetchmany(1)
        
        #showing the rows
        for row in rows:
        #    print(row)
            x.append(row)
        #print(x)    
            #c.executemany('INSERT INTO students VALUES(?,?,?);',records);
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
    #all_db.close()
    
    
    def uploadData(self,c_count, shop_Number):
                
        self.createDB()
        self.recursive_items(c_count)
        self.CalculatingTheAmount()
        self.querySales()
        self.calculateSales()
        self.testDB(shop_Number)
        
    def recursive_items(self,dictionary):
        
        logging.info('Start add DB from 1C')
        count = 0
        for key  in dictionary:
          #  print(key)
            self.addRecord(dictionary[key],key)
            count = count + len(dictionary[key])
        
        logging.info('End add DB from 1C')    
        logging.info('added - ' + str(count) + ' records')    


    def CalculatingTheAmount(self):
        """Запускает SQL скрипт, который переносит количество с аналагов пива на головную номенклатуру"""        
        pathScript = Path("data", "upd.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        logging.info('Summ analog calcalating')  

    def addRecord(self,item_position,key):

        self._cursor.execute('PRAGMA synchronous = OFF')

        if key == 'invent':
            self._cursor.executemany(diff_data.qrAddinvent, item_position,)
        elif key == 'additionalprices':
            self._cursor.executemany(diff_data.qrAddadditionalprices, item_position,)   
        elif key == 'barcodes':
            self._cursor.executemany(diff_data.qrAddBarcodes, item_position,)   
        elif key == 'inventitemoptions':
            self._cursor.executemany(diff_data.qrAddinventitemoptions, item_position,)       
        elif key == 'priceoptions':
            self._cursor.executemany(diff_data.qrAddPriceoptions, item_position,)                   
        elif key == 'quantityoptions':
            self._cursor.executemany(diff_data.qrAddquantityoptions, item_position,)                               
        elif key == 'sellrestrictperiods':
            self._cursor.executemany(diff_data.qrAddSellrestrictperiods, item_position,)                                           

        self._cursor.execute(diff_data.qrAddOptions)
        
        self._all_db.commit() 
        
        
    def calculateSales(self):
        """Запускает SQL скрипт, который отнимает проданное от пришедшего товара"""        
        pathScript = Path("data", "updateprod.sql") 
        with open(pathScript, 'r') as sql_file:
            sql_script = sql_file.read()
        self._cursor.executescript(sql_script)
        logging.info('Sales calcalating')              
        
        
    def testDB(self,shop_Number):
        """Maps a number from one range to another.
    :param number:  The input number to map.
    :param in_min:  The minimum value of an input number.
    :param in_max:  The maximum value of an input number.
    :param out_min: The minimum value of an output number.
    :param out_max: The maximum value of an output number.
    :return: The mapped number.
    """
    
        #self._cursor.execute("select * from invent")
        #sql - это ваш cursor
        #massive = self._cursor.fetchone()#этот метод вернет вам один кортеж с только одной строкой из базы
        #  massive_big = self._cursor.fetchall()#этот метод вернет вам все элементы в одном кортеже. Данные из строк будут представлены как вложенные кортежи
        #перебираем обычный кортеж, просто печатаем элементы кортежа
        #for i in range(len(massive)):
        #    print(massive[i])
        
        if sys.platform.startswith("linux"):  # could be "linux", "linux2", "linux3", ...
                self._all_db.row_factory = pysqlite3.Row # Позволяет работать с возвращаемым результатам с обращением к столбцам по имени
        elif sys.platform == "darwin":
            pass
        elif sys.platform == "win32":
            self._all_db.row_factory = sqlite3.Row
        
        #outfile = open('tData.aif', 'w',encoding='utf-8')  
        curFileName = 'pos' + str(shop_Number) + '.aif'
        pathAif = Path("upload", curFileName) 
        outfile = open(pathAif, 'w',encoding='utf-8')  
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
                
                #outfile.writelines(str(nDict))
                #outfile.writelines(diff_data.separator)
                
                json.dump(dictForArtix, outfile,  indent=2,  ensure_ascii=False )
                
                outfile.write('\n' + diff_data.separator + '\n')    
            else:
                break    
        outfile.write(diff_data.footer)  
        
        #pathAif
        sendFile.sendFile(pathAif,shop_Number)
        #
        # src =  pathAif
        # dst = '//192.168.0.239/obmen/dict/'+ curFileName
        # shutil.copyfile(src, dst)
        #перебираем кортеж с кортежами внутри, также печатаем элементы
        #for z in range(len(massive_big)):
        #    print(massive_big[z])        
        #{"command":"addInventItem",                
        
        
        
        ''' def send_request(c_shop,server_ip,port):
     # print(main.rc.get('artix','server_ip'))
     try:
         
          r = requests.get('http://' +server_ip + ':' + port + '/UNF_test/hs/test_s/V1/test')
          #r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
          r.encoding = 'utf-8' 
          print(r.status_code)
          c_count = r.json()
          #c_count = json.loads(r.text)
         # print(c_count)    
          return c_count
     except Exception as e:
          logging.exception(e, exc_info=False)
          return None
     

 '''
 
 
 # src =  pathAif
        # dst = '//192.168.0.239/obmen/dict/'+ curFileName
        # shutil.copyfile(src, dst)
        #перебираем кортеж с кортежами внутри, также печатаем элементы
        #for z in range(len(massive_big)):
        #    print(massive_big[z])        
        #{"command":"addInventItem",
        
        
        
        