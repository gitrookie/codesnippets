import logging

# create logger
module_logger = logging.getLogger("spam.auxiliary_module")


class Auxiliary:
    def __init__(self):
        self.logger = logging.getLogger("spam.auxiliary_module.Auxiliary")
        self.logger.info("Creating instance of Auxiliary")

    def do_something(self):
        self.logger.info('Doing Something')
        a = 1 + 1
        self.logger.info("Done Doing Something")


def some_function():
    module_logger.info("Received a call to some_function")
