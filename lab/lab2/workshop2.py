import paramiko
import logging
import time

def database_name():
    return time.strftime("%Y-%m-%d")+".sql"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('10.0.99.99', username='python03', password='python03')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

sftp = ssh.open_sftp()
# get .sql file from server
sftp.get('/home/python03/backup_testdb.sql', database_name())

sftp.close()

ssh.close()
