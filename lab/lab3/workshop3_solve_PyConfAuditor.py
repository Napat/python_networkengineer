import logging
import crassh

banner = '''
     ______            _____                        __  _                ___             ___ __            
  / ____/___  ____  / __(_)___ ___  ___________ _/ /_(_)___  ____     /   | __  ______/ (_) /_____  _____
 / /   / __ \/ __ \/ /_/ / __ `/ / / / ___/ __ `/ __/ / __ \/ __ \   / /| |/ / / / __  / / __/ __ \/ ___/
/ /___/ /_/ / / / / __/ / /_/ / /_/ / /  / /_/ / /_/ / /_/ / / / /  / ___ / /_/ / /_/ / / /_/ /_/ / /    
\____/\____/_/ /_/_/ /_/\__, /\__,_/_/   \__,_/\__/_/\____/_/ /_/  /_/  |_\__,_/\__,_/_/\__/\____/_/     
                       /____/                                                                            
'''
print(banner)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt="%d/%m/%Y %H:%M:%S")
logger = logging.getLogger("ConfAuditor")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('ConfAuditor.log')
handler.setFormatter(formatter)
logger.addHandler(handler)

routers = ["10.1.0.11", "10.1.0.12", "10.1.0.13"]
username = "admin"
password = "admin1234"

logger.info("Configuration Auditor Scaning ...")
print("Configuration Auditor Scaning...")

for device in routers:
    try:
        hostname = crassh.connect(device, username, password)
        output = crassh.send_command("show run | include snmp-server", hostname)
        crassh.disconnect()

        # Split the output by spaces 
        words = output.split()
        logger.info("Scan Configuration on %s [%s]" % (hostname, device))

        # Look for "public"
        for word in words:
            if word == "public":
                logger.warning("Found Default SNMP Community!! on %s [%s]" %(hostname, device))
    except:
        logger.error("Cannot connect to %s" %device)
        pass  # If connect fails, move onto next router in the list.

logger.info("Configuration Auditor Program Stop.")
print("Done !")