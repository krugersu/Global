# app_logger.py

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path  



def get_logger(name):
    
    pathLOG = Path("log", "py_log.log") 
    
    logging.basicConfig(level=logging.DEBUG, filename=pathLOG,
        filemode="a", 
        format=u"%(asctime)s [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d)  %(message)s"
        ,datefmt='%Y-%m-%d %H:%M:%S',) 
    
    logger = logging.getLogger(name)
    ''' handler = RotatingFileHandler('py_log.log', maxBytes=20, backupCount=5)
    logger.addHandler(handler) '''
    return logger