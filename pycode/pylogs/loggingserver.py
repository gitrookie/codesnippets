import logging
import logging.config
import time
import os
import json

with open("logging.conf", "r") as fd:
    logging.config.fileConfig(fd)
t = logging.config.listen(9999)
t.start()

logger = logging.getLogger()

try:
    while True:
        logger.debug(t)
        logger.debug("debug message")
        logger.info("info message")
        logger.warn("warn message")
        time.sleep(10)
except KeyboardInterrupt:
    logging.config.stopListening()
    t.join()
        
