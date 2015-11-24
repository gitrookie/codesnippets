import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


app = QApplication(sys.argv)

try:
    due = QTime.currentTime()
    message = "Alert!"
    if len(sys.argv) < 2:
        raise ValueError
    hours, mins = sys.argv[1].split(":")
    due = QTime(int(hours), int(mins))

    if not due.isValid():
        raise ValueError
    if len(sys.argv) > 2:
        message = " ".join(sys.argv[2:])
except ValueError:
    message = "Usage: alert.pyw HH:MM [optional message]" # 24hr clock

while QTime.currentTime() < due:
    time.sleep(20) # 20 seconds

label = QLabel("<font color=red size=72><b>" + message + "</b></font>")
# label.setWindowFlags(Qt.SplashScreen)
label.show()
QTimer.singleShot(60000, app.quit) # 1 minute

app.exec_()
# So we have two events scheduled. A paint event that wants to take place
# immediately, and a timer timeout event that wants to take place in minute's
# time. The call to app.exec_() starts off the QApplication object's event loop.
# The first event it gets is the paint event, so the label window pops up
# on-screen with the given message. About one minute later the timer timeout
# event occurs and the QApplication.quit() method is called. The method
# clean termination of the GUI application. It closes any open windows, frees up
# any resources it has acquired, and exits.
