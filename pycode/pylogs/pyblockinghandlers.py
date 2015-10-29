# Blocking Handlers
import queue
import logging
from logging.handlers import QueueHandler, QueueListener

que = queue.Queue(-1)
queue_handler = QueueHandler(que)
handler = logging.StreamHandler()
listener = QueueListener(que, handler)
root = logging.getLogger()
root.addHandler(queue_handler)
formatter = logging.Formatter("%(threadName)s: %(message)s")
handler.setFormatter(formatter)
listener.start()
root.warning("Look Out")
listener.stop()
