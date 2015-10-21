import logging
# logger objects are never instantiated directly, but always through module
# level function logging.getLogger(name) as follows which returns the
# logging.Logger object as follows
logger = logging.getLogger(__name__)
print(logger.propagate)
