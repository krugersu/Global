import configparser

import logging
import os
import main


# AttrDict - это класс, производный от dict который позволяет получить доступ как через ключи словаря,
# так и через доступ к атрибутам: это означает a.x is a['x']
# мы можем использовать этот класс в ConfigParser:
class AttrDict(dict):
    def __init__(self, *args, **kwargs):
        super(AttrDict, self).__init__(*args, **kwargs)
        self.__dict__ = self

class m_Config:
    
    pathConfFile = '/config.ini'
    devpathConfFile = './config/config.ini'

    def __init__(self):  
        pass

    def loadConfig(self):
        
        conf = configparser.ConfigParser(dict_type=AttrDict)
      #  conf.sections()
        if os.path.exists(self.devpathConfFile):
            conf.read(self.devpathConfFile,encoding="utf-8")
        else:
            logging.error('File .ini not exist')
            return None
        return conf
    