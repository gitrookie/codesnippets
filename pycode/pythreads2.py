import sys
import time
import signal
import threading

# Setting up quitter Object stars with value False
quitter = threading.Event()
quitter.clear()


def signal_handler(signum, frame):
    print("Killing Threads")
    quitter.set()
    for t in threading.enumerate():
        if not t == threading.current_thread():
            t.join()


def looper():
    x = 0
    while True:
        x += 1
        time.sleep(1)
        if quitter.is_set():
            print("Quitting Thread...")
            break


def main():
    for x in range(4):
        t = threading.Thread(target=looper)
        t.start()
    time.sleep(2)

    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    while threading.active_count() > 1:
        print("Currently %d threads running" % threading.active_count())
        time.sleep(4)
    print("Main thread done")
    sys.exit(0)

main()
