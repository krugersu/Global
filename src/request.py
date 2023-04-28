
import logging
import requests
import main
import json
import os
import pathlib
from pathlib import Path
import tortilla
from pprint import pprint

from requests.auth import HTTPBasicAuth

import settings
import logging.config


#logger = app_logger.get_logger(__name__)
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger('my_logger')


class req1C:
     def __init__(self, nConfig):
          self.mConfig = nConfig
          
     def __enter__(self):
          return self

     def __exit__(self):
          self.close()
          
     def exeQuery(self,c_shop):
          try:
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery,  auth=('Adm', ''))
# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test')
               r.encoding = 'utf-8' 
               c_count = r.json()
               return c_count
          except Exception as e:
               logger.exception(e, exc_info=False)
          return None
     
     
     
     
     def getQueryShop(self):
                    
          try:
              
               r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.shopquery,  auth=('Adm', ''))  #  ,auth=('Adm', ''))
                    
               r.encoding = 'utf-8' 
               c_count = r.json()
               listShop = self._getDirM(c_count)
               return listShop  # c_count
          except Exception as e:
               logger.exception(e, exc_info=False)
          return None     

     def shopForNumber(self,c_shop):
          
          mPar = {"number":str(c_shop)}
          print(mPar) 
          try:
               # r = requests.get('http://' + self.mConfig._sections.one_C.server_ip + ':' 
               #                     + self.mConfig._sections.one_C.port 
               #                     + self.mConfig._sections.one_C.lquery, params=mPar)
               
               n_shop = tortilla.wrap('http://' + self.mConfig._sections.one_C.server_ip + ':' 
                                   + self.mConfig._sections.one_C.port 
                                   + self.mConfig._sections.one_C.lquery,  auth=('Adm', '')) #,  auth=('Adm', '')
               c_count = n_shop.test_s.get('V1/GetProductRemains?number=' +str(c_shop))
               
               

# ?  r = requests.get('http://192.168.252.250:8082/UNF_test/hs/test_s/V1/test_1')

              # c_count = r.json()
               return c_count
          except Exception as e:
               logger.exception(e, exc_info=False)
          return None



     def _getDirM(self,listPath):
          
          listShop = []
          
          for curPath in listPath:
               curPath.replace('\\\\', '//')
               curPath = pathlib.PureWindowsPath(curPath)
               listShop.append(Path(curPath).parts[-1])
               listShop = list(set(listShop))
          return listShop
          



#******************************   Work workshift **************************************************************************************


     def post_workshift(self,l_workshift):
          
          try:
               r = requests.post('http://' + self.mConfig._sections.one_C.server_ip + ':'
                                   + self.mConfig._sections.one_C.port
                                   + self.mConfig._sections.one_C.workshift,   auth=('Adm', ''),data=None, json = l_workshift)
          
          except Exception as e:
               logging.info('status_code - ' + str(r.status_code))
               logging.exception(e, exc_info=False)
               
          return (r.status_code)

     def post_workshift_open(self,l_workshift_open):
          
          try:
               r = requests.post('http://' + self.mConfig._sections.one_C.server_ip + ':'
                                   + self.mConfig._sections.one_C.port
                                   + self.mConfig._sections.one_C.workshift_open,   auth=('Adm', ''), data=None, json = l_workshift_open)
               
          except Exception as e:
               logging.info('status_code - ' + str(r.status_code))
               logging.exception(e, exc_info=False)
               
          return (r.status_code)