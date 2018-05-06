import logging
import paramiko
import time

host = '203.209.49.76'
hostuser = 'admin'
hostpass = '123456'
filename = time.strftime("%Y-%m-%d")

cmd01 = "mysqldump -uadmindb -padmindbpass testdb > " + filename

logger = logging.getLogger("PyBackup")
logger.setLevel(logging.DEBUG)

# create a file handler
handler = logging.FileHandler('PyBackup.log')

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%d/%m/%Y - %H:%M:%S")
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(host, username=hostuser, password=hostpass)
    logger.info('Connect to Server Success')
    ssh.exec_command(cmd01)
    sftp = ssh.open_sftp()
    sftp.get('/home/admin/' + filename, filename + '.sql')
    sftp.close()
    ssh.close()
    logger.info('Backup Successfully')
except paramiko.SSHException:
    logger.error('Connection Fail!!')
    quit()


