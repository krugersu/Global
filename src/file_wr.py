#! /usr/bin/python
# -*- coding: utf-8 -*-
import logging
import os
from os.path import *
from pathlib import Path
import app_logger
import settings
import logging.config


#logger = app_logger.get_logger(__name__)
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger('my_logger')

#Функция ищет все файлы с расширением ".flg" во всех подкаталогах каталога 

def find_change(catalog, f):
# ?
    find_files = []
    
    root_directory = Path(catalog)
    print(root_directory)
    if root_directory.exists(): 
        for path_object in root_directory.rglob('*.flg'):
            if path_object.is_file():
                find_files.append(path_object.parts[1])
        logger.info("Изменения в магазинах - " +  ','.join(find_files))            
    else:
        logger.info("Сервер 1С не доступен")    
    return find_files

    
