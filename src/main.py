#/usr/bin/env python3.11
"""Example Python program with Sphinx style comments.
Description
-----------
Example Python program with Sphinx style (reStructuredText) comments.
Libraries/Modules
-----------------
- time standard library (https://docs.python.org/3/library/time.html)
    - Access to sleep function.
- sensors module (local)
    - Access to Sensor and TempSensor classes.
Notes
-----
- Comments are Sphinx (reStructuredText) compatible.

----
- None.
Author(s)
---------
- Created by John Woolsey on 05/27/2020.
- Modified by John Woolsey on 07/02/2020.
Copyright (c) 2020 Woolsey Workshop.  All rights reserved.
Members
-------
"""
# Imports
import os
import sys
import configparser
import m_config
from requests.exceptions import HTTPError
import schedule, time
import file_wr, request
import app_logger
import db
import dbMysql
import pathlib
from pathlib import Path 
import workDB
import tlgrm
import create_aif
import request

#: Global Constants
logger = app_logger.get_logger(__name__)
cPath = Path(os.getcwd())
cPath.joinpath('Global', 'src')
# fileinit = '/home/administrator/Global/src/first.dat'
# sys.path.insert(1,'/home/administrator/Global/src/')
fileinit = '/home/bat/Project/Python/Kruger/Global/src/first.dat'
sys.path.insert(1,'/home/bat/Project/Python/Kruger/Global/src/')
"""Для логирования событий"""




# ! Посмотреть как работает sqlite с json https://habr.com/ru/post/528882/
# ! Подумать о хранении таблиц БД в памяти
# ! Что делать если таблица рухнет в процессе расчета?


# Functions
def main():
   """ Main program entry. """
   # Если это первый запуск системы
   if not os.path.exists(fileinit):
      with open(fileinit, 'w', encoding='utf-8') as outfile:
            outfile.write('')    
            init_pr()

   
   path = Path("config", "config.ini") 
   logger.info("Start programs")
   logger.info("Current path " + str(cPath))

   
   f = '*flg'
   #tlgrm.send_telegram("Start programs")
   #catalog = rc._sections.one_C.cat_skl
   #c_shop = file_wr.find_change(catalog, f)
   
   
   
   c_shop = []
   # Apoc по магазинам с изменения
   tData = dbMysql.workDb(rc)
   rec_con = request.req1C(rc)
   mCount = request.req1C(rc)
   
   # Список открытых смен от последнего зафиксированного времени
   l_workshift_open = tData.get_last_workshift_open()
   logger.info(u'Number of open cash shifts - ' + str(len(l_workshift_open)))
   # Если нечего отправлять, то и не отправляем
   if len(l_workshift_open) > 0:
      status_code = rec_con.post_workshift_open(l_workshift_open)
      # Меняем дату в файле только в случае успешного результата работы 1С
      if status_code == 200:
            tData.save_new_date_open()
      else:
            logger.warning('status_code_open - ' + str(status_code ))
            
            
   # Список закрытых смен от последнего зафиксированного времени
   l_workshift = tData.get_last_workshift()
   logger.info(u'Number of closed cash shifts - ' + str(len(l_workshift)))
   # Если нечего отправлять, то и отправляем
   if len(l_workshift) > 0:
      #rec_con = m_request.req1C(rc)
      status_code = rec_con.post_workshift(l_workshift)
      # Меняем дату в файле только в случае успешного результата работы 1С
      if status_code == 200:
            tData.save_new_date()
      else:
            logger.warning('status_code - ' + str(status_code ))
   
   tData.close_db_connection()      
   
   
   # Анализ в каких магазинах изменения
   c_shop = mCount.getQueryShop()
   #print(c_shop)
   # Обработка данных по магазинам
   for curShop in c_shop:
   #   print(curShop)    
      c_count = mCount.shopForNumber(curShop)
      if not c_count == None:  
         tData = db.workDb(rc)
         tData.uploadData(c_count, curShop)
   
   logger.info(u'End programs')   
   logger.info(u'*****************************************************************')   

   tData.close_db_connection()

def init_pr():

   filename = '/home/administrator/Workshift_load/src/last_date.txt'
   if not os.path.exists(filename):
      with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('1')#'2023-01-01 00:00:00'
            
   filename = '/home/administrator/Workshift_load/src/last_date_open.txt'
   if not os.path.exists(filename):
      with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('1')  # '2023-01-01 00:00:00'


#schedule.every(10).seconds.do(job1, p='Через 10 секунд')



if __name__ == "__main__":

   # schedule.every(1).minutes.do(main)
   m_conf = m_config.m_Config()   
   rc =  m_conf.loadConfig()
   #exec(open("test2.py").read())
   if not rc == None:
      main()
   else:
      logger.error('Configuration file not found')
      logger.info('The program has finished its work')
      
   #while True:
   #    schedule.run_pending()
   #    time.sleep(1)


##FIX  Не выгружается объем тары
#TODO Обработать ситуацию, когда головной номенклатуры нет на остатке и она не попадает в выгрузку. Т.е. головная номенклатура должна выгружаться всегда
#TODO Чтение файла конфигурации в попытку
#FIXME Исправить подписку на событие согласно текстовым номерам магазинов и новому реквизиту
## FIX Не выгружать штрихкод
## FIX Разобраться с группой товаров