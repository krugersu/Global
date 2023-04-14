
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



def sendFile(fileName,shopNumber,typeFile):
    
    nameFileDest = 'pos'
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=secret,timeout=4)
    # time.sleep(1)
    # ssh.connect('127.0.0.1', username='bat', 
    #     password='Uytplj12')
    # stdin, stdout, stderr =ssh.exec_command("uptime")
    
    # stdout.readlines()
    ftp = ssh.open_sftp()
    if typeFile:
        ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        #ftp.put('./upload/'+fileName.name, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        ftp.put('/home/administrator/Global/upload/'+fileName.name, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.aif')
        
      #  shutil.copyfile('/home/bat/Project/Python/Kruger/Artix_gen/upload/postest.aif', '/mnt/share/test/postest.aif')
        # source = Path('/home/bat/Project/Python/Kruger/Artix_gen/upload/test.aif')
        # destination = Path('/mnt/share/test/postest.aif')
        # destination.write_bytes(source.read_bytes())
        print(fileName)
      #  print('./upload/'+fileName.name)
      #  print(shopNumber)
        print('Upload finished_1')
    else:    
        ftp.put(fileName, '/opt/OBMEN/dict/'+ shopNumber +'/' + 'pos'+ shopNumber+'.flz')
     #   shutil.copyfile('./upload/'+fileName.name, '/mnt/share/'+ shopNumber +'/' + 'pos'+ shopNumber+'.flz')
     #   time.sleep(5)
        print('Upload finished_2')
    # ftp.close()
    # ssh.close()
    