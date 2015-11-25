# signalandslots.py
# Example shows how two widgets are interconnected using signal and slots.
# Emitting Custom Signals in PyQt5
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from functools import partial

class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__()
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)
        spinbox.valueChanged.connect(dial.setValue)
        self.setWindowTitle("Signals and Slots")


# Emitting Custom Signals
class ZeroSpinBox(QSpinBox):

    zeros = 0
    csig = pyqtSignal("int")         # pyqtSignal is factory function
    def __init__(self, parent=None):
        super().__init__()
        self.valueChanged.connect(self.checkzero)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.csig.emit(self.zeros)


class Form2(QDialog):

    def __init__(self, parent=None):
        super().__init__()
        dial = QDial()
        dial.setNotchesVisible(True)
        spinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        dial.valueChanged.connect(spinbox.setValue)
        spinbox.csig.connect(self.announce)
        self.setWindowTitle("Signals and Slots")

    def announce(self, zeros):
        print("ZeroSpinBox has been at %d times" % zeros)




class TaxRate(QObject):
    rateChanged = pyqtSignal("float")

    def __init__(self):
        super().__init__()
        self.__rate = 17.5

    def rate(self):
        return self.__rate

    def setRate(self, rate):
        if rate != self.__rate:
            self.__rate = rate
            self.rateChanged.emit(self.__rate)


def rateChanged(rate):
    print("Rate Changed to {}".format(rate))


# t = TaxRate()
# t.rateChanged.connect(rateChanged)
# t.setRate(8.23)


class Form3(QDialog):

    def __init__(self, parent=None):
        super().__init__()

        button1 = QPushButton("One")
        button2 = QPushButton("Two")
        button3 = QPushButton("Three")
        button4 = QPushButton("Four")
        self.label = QLabel("Click a Button")

        layout = QVBoxLayout()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.button1callback = partial(self.anybutton, "one")
        self.button2callback = partial(self.anybutton, "two")
        self.button3callback = partial(self.anybutton, "three")
        self.button4callback = partial(self.anybutton, "four")

        button1.clicked.connect(self.button1callback)
        button2.clicked.connect(self.button2callback)
        button3.clicked.connect(self.button3callback)
        button4.clicked.connect(self.button4callback)

    def anybutton(self, args):
        self.label.setText("You Clicked Button %s" % args)

app = QApplication(sys.argv)
form = Form3()
form.show()
app.exec_()
