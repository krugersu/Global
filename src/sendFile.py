
import paramiko
import time
import shutil
from pathlib import Path

import settings
import logging.config


#logger = app_logger.get_logger(__name__)
logging.config.dictConfig(settings.LOGGING_CONFIG)
logger = logging.getLogger('my_logger')

host = '10.0.0.239'
user = 'administrator'
secret = 'adm@#747911ART'
port = 22


#!!!!!!!!!!!!!!!!  Если будут ошибки при выгрузке и не будет работать - уброать try exept и  ssh.close()
     

def sendFile(fileName,shopNumber,typeFile):
    
    nameFileDest = 'pos'
    try:
      ssh = paramiko.SSHClient()
      ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
      ssh.connect(host, username=user, password=secret,timeout=4)
    
      ftp = ssh.open_sftp()
      if typeFile:
          ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        #ftp.put('./upload/'+fileName.name, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
          ftp.put('/home/administrator/Global/upload/'+fileName.name, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        
          logger.info('Upload file *aif - ' + fileName.name)
          logger.info(fileName)
      else:    
          ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.flz')
          logger.info('Upload file *flz - ' + fileName.name)
          logger.info(fileName)
    except (paramiko.AuthenticationException,
                paramiko.ssh_exception.NoValidConnectionsError) as e:
            logger.error(e)
    except paramiko.SSHException as e:
            logger.error(e)
            
    # ftp.close()
    ssh.close()
    