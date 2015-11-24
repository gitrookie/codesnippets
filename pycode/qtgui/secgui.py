# secgui.py

import sys
from math import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Form(QDialog):

    def __init__(self, parent=None):
        # Widget with no parent becomes a top-level window
        super().__init__()
        self.browser = QTextBrowser()

        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)

        self.lineedit.setFocus()

        # Old style signals and slots not valid for PyQt5
        # self.connect(self.lineedit, SIGNAL("returnPressed()"), self.updateUi)
        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle("Calculate")

    def updateUi(self):
        try:
            text = self.lineedit.text
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
        except:
            self.browser("<font color=red>%s is invalid!</font>" % text)

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
