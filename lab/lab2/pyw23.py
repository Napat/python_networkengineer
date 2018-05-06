import logging

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s' \
,datefmt="%d/%m/%Y %H:%M:%S")

logger = logging.getLogger("Logger")

# write only level higher than INFO
## debug, info -> not write
## warning, error, critical -> write
logger.setLevel(logging.WARNING)

# create a file handler
handler = logging.FileHandler('testlog.log')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.debug("Message01")
logger.info("Message02")    
logger.warning("Message03")
logger.error("Message04")
logger.critical("Message05")

logger.removeHandler(handler)

""" Output case: logger.setLevel(logging.INFO)
06/05/2018 14:54:44 - Logger - INFO - Message02
06/05/2018 14:54:44 - Logger - WARNING - Message03
06/05/2018 14:54:44 - Logger - ERROR - Message04
06/05/2018 14:54:44 - Logger - CRITICAL - Message05
"""

""" Output case: logger.setLevel(logging.WARNING)
06/05/2018 14:54:44 - Logger - INFO - Message02
06/05/2018 14:54:44 - Logger - WARNING - Message03
06/05/2018 14:54:44 - Logger - ERROR - Message04
06/05/2018 14:54:44 - Logger - CRITICAL - Message05
"""
