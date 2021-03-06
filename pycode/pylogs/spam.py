import logging
import auxiliary_module

# create logger with spam application
logger = logging.getLogger("spam")
logger.setLevel(logging.DEBUG)
# create filehandler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to handlers
formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(ch)
logger.addHandler(fh)

logger.info("Creating an instance of auxiliary_module.Auxiliary")
a = auxiliary_module.Auxiliary()
logger.info("created an instance of auxiliary_module.Auxiliary")
logger.info("Calling auxiliary_module.Auxiliary.do_something")
a.do_something()
logger.info("finished auxiliary_module.Auxiliary.do_something")
logger.info("calling auxiliary_module.some_function()")
auxiliary_module.some_function()
logger.info("Done with auxiliary_module.some_function()")
