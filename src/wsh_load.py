#!/usr/bin/python3.10

import os
import sys
import configparser
import m_config
import m_request


import app_logger
import db
import pathlib
from pathlib import Path 

#: Global Constants
logger = app_logger.get_logger(__name__)
cPath = Path(os.getcwd())
cPath.joinpath('Workshift_load', 'src')
fileinit = '/home/administrator/Workshift_load/src/first.dat'
sys.path.insert(1,'/home/administrator/Workshift_load/src/')
"""Для логирования событий"""



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
    
    
    tData = db.workDb(rc)
    rec_con = m_request.req1C(rc)

    
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
    
    logger.info('Normal shutdown of the program')
    logger.info('******************************************************************************************************************')

def init_pr():
    
    filename = '/home/administrator/Workshift_load/src/last_date.txt'
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('1')#'2023-01-01 00:00:00'
            
    filename = '/home/administrator/Workshift_load/src/last_date_open.txt'
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as outfile:
            outfile.write('1')  # '2023-01-01 00:00:00'

if __name__ == "__main__":

    # Чтение настроек
    m_conf = m_config.m_Config()   
    rc =  m_conf.loadConfig()
    if not rc == None:
        main()
    else:
        logger.error('Configuration file not found')
        logger.info('The program has finished its work')


