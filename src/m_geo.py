





import time

https://github.com/krugersu/Artix_gen/blob/main/src/m_geo.py

import paramiko

host = '192.168.0.239'
user = 'administrator'
secret = '*********'
port = 22


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy())

ssh.connect(host, username=user, 
    password=secret)
# ssh.connect('127.0.0.1', username='bat', 
#     password='Uytplj12')
# stdin, stdout, stderr =ssh.exec_command("uptime")
# time.sleep(1)
# stdout.readlines()
ftp = ssh.open_sftp()
ftp.put('./test.py', '/opt/OBMEN/dict/test1.py')
ftp.close()
