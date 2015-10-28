import socket
import os
import logging
import select

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pyserver")

inp = []
out = []
errlist = []

sock_file = "./pysocket.sock"
logger.debug("Creating Socket...")
s = socket.socket(family=socket.AF_UNIX, type=socket.SOCK_STREAM)
logger.debug("Created Socket...%s %s" % (s, type(s)))
logger.debug("Binding Socket...")
s.bind(sock_file)
logger.debug("Bound Socket...")
logger.debug("Trying to Listening Socket...")
s.listen(5)
logger.debug("Listening Socket...")
try:
    while True:
        logger.debug("Accept call on Socket...")
        connection, client_address = s.accept()
        inp.append(connection)
        logger.info("---%s %s---" % (connection, client_address))
        connection.setblocking(False)
        logger.debug("Socket call accepted...%s %s" % (connection,
                                                       type(connection)))
        while True:
            try:
                logger.debug("Calling Select...")
                inp_ready, out_ready, err = select.select(inp, out, errlist)
                logger.debug("Connection is ready...")
                data = connection.recv(8)
                print(data)
                if not data:
                    break
            except socket.error as e:
                logger.exception(e)
                pass
finally:
    os.remove(sock_file)
    connection.close()

logger.info("Server has been closed")
