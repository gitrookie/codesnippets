import logging
import myapp
# logger objects are never instantiated directly, but always through module
# level function logging.getLogger(name) as follows which returns the
# logging.Logger object as follows
# logger = logging.getLogger(__name__)

# Setting Level to "debug" will log all the messages

# logging.basicConfig(filename="test.log", level=logging.DEBUG,
#                     format="%(asctime)s %(levelname)s %(message)s")
# logging.debug("This msg is for file")
# logging.info("Logging Module: info")
# logging.warning("Logging module: warning")
# x = 10
# myapp.foo()

# Root logger has an explicit level set (WARNING by default). When deciding
# wether to process an event, the effective level of the logger is used to
# determine wether to pass event to logger's handlers. Child loggers propagate
# messages to the handlers associated with their ancestor loggers. Because of
# this it is unncesscary to define and configure handlers for all the loggers
# an application uses. It is sufficient to configure handlers for top level
# logger and create child loggers as needed.


logger = logging.getLogger("pylogs")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

fh = logging.FileHandler(filename="test.log")
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s -%(name)s - %(levelname)s - %(message)s")
# ch.setFormatter(formatter)
fh.setFormatter(formatter)
logger.addHandler(ch)
logger.addHandler(fh)

logger.debug("debug message")
logger.info("info message")
logger.warn('warn message')
logger.error("error message")
logger.critical("critical message")

# Logging messages are encoded as instances of the LogRecord class. When a
# logger decides to actually log an event, a LogRecord instance is created
# from the logging message.
