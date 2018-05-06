import crassh
import logging

# High rank user, no need to Enablepass
router = "10.0.1.22"
username = "admin"
password = "admin1234"
cmd01 = "show running-config"
output = ""

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt="%d/%m/%Y %H:%M:%S")
logger = logging.getLogger("Logger")
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('testlog.log')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

try:
    hostname = crassh.connect(router, username, password)
    #print("Connected device %s [%s]" % (hostname, router))
    output = crassh.send_command(cmd01, hostname)
    #print(output)

    crassh.disconnect()

except:
    print("Can not connect to [%s]" % router)

# search output for text "snmp-server community public"
if output.find('snmp-server community public') != -1:
    print('found')
    logger.warning("router ip address " + router +
                   " set snmp-server community to public")
else: 
    print('Not found')
