import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect('10.0.99.99', username='python03', password='python03')
except paramiko.SSHException:
    print("Connection Failed")
    quit()

print("-----")
stdin, stdout, stderr = ssh.exec_command("pwd")
for line in stdout.readlines():
    print(line.strip())

print("-----")
stdin, stdout, stderr = ssh.exec_command("who")
for line in stdout.readlines():
    print(line.strip())

print("-----")
stdin, stdout, stderr = ssh.exec_command("mysql -uroot -pMNRpythonadmin -e 'use mysql; show tables'")
for line in stdout.readlines():
    print(line.strip())

print("-----")
stdin, stdout, stderr = ssh.exec_command("mysql -uroot -pMNRpythonadmin -e 'show databases;use mysql; show tables'")
for line in stdout.readlines():
    print(line.strip())

ssh.close()


""" Output
-----
/home/python03
-----
python29 pts/0        2018-05-06 21:16 (10.0.1.163)
python20 pts/1        2018-05-06 21:19 (10.0.1.180)
python17 pts/2        2018-05-06 21:21 (10.0.1.198)
python39 pts/3        2018-05-06 21:22 (10.0.1.169)
python03 pts/4        2018-05-06 21:26 (10.0.1.158)
python18 pts/5        2018-05-06 21:22 (10.0.1.172)
-----
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
-----
Database
information_schema
mnr_python
mysql
performance_schema
Tables_in_mysql
columns_priv
db
event
func
general_log
help_category
help_keyword
help_relation
help_topic
host
ndb_binlog_index
plugin
proc
procs_priv
proxies_priv
servers
slow_log
tables_priv
time_zone
time_zone_leap_second
time_zone_name
time_zone_transition
time_zone_transition_type
user
"""
