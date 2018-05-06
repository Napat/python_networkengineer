import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('10.0.99.99', username='python03', password='python03')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

"""
print("-----")
stdin, stdout, stderr = ssh.exec_command("mysqldump -uadmindb -padmindbpass testdb > backup_testdb.sql")
for line in stdout.readlines():
    print(line.strip())
"""

print("-----")
sftp = ssh.open_sftp()
# get .sql file from server
sftp.get('/home/python03/backup_testdb.sql','backup_testdb.sql')   
# put .png file to server
sftp.put("pinggraph.png", "/home/python03/pinggraph.png")

sftp.close()

ssh.close()


