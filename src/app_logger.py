# app_logger.py

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path  



def get_logger(name):
    
    #pathLOG = Path("log", "ws_log.log") 
    pathLOG = "/home/administrator/Global/log/ws_log.log"
    #pathLOG = "/home/bat/Project/Python/Kruger/Global/log/ws_log.log"
    
    #pathLOG = Path("./log", "py_log.log") 
    #print(pathLOG)
    logging.basicConfig( handlers=[RotatingFileHandler(
        
        '/home/administrator/Global/log/ws_log.log', maxBytes=2000000, backupCount=10)],level=logging.DEBUG, 
        #'/home/bat/Project/Python/Kruger/Global/log/ws_log.log', maxBytes=2000000, backupCount=10)],level=logging.DEBUG, 
        
        format=u"%(asctime)s | [%(levelname)s] | (%(filename)s).|%(funcName)s(%(lineno)d) | %(message)s"
        ,datefmt='%Y-%m-%d %H:%M:%S',) 
    
    logger = logging.getLogger(name)
    
    return logger




def get_logger_old(name):

    # pathLOG = Path("log", "ws_log.log")
    pathLOG = "/home/administrator/Global/log/ws_log.log"

    # pathLOG = Path("./log", "py_log.log")
    print(pathLOG)
    logging.basicConfig(level=logging.DEBUG, filename=pathLOG,
                        filemode="a",
                        format=u"%(asctime)s [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d)  %(message)s", datefmt='%Y-%m-%d %H:%M:%S',)

    logger = logging.getLogger(name)
    ''' handler = RotatingFileHandler('py_log.log', maxBytes=20, backupCount=5)
    logger.addHandler(handler) '''
    return logger

#format=u"%(asctime)s [%(levelname)s] - (%(filename)s).%(funcName)s(%(lineno)d)  %(message)s"