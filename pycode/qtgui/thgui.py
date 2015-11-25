# thgui.py
# Small GUI App for currency converter

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from urllib.request import urlopen


class Form(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        date = self.getdata()
        rates = sorted(self.rates.keys())

        dateLabel = QLabel(date)
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01, 10000000.00)
        self.fromSpinBox.setValue(1.00)
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        self.toLabel = QLabel("1.00")

        grid = QGridLayout()
        grid.addWidget(dateLabel, 0, 0)
        grid.addWidget(self.fromComboBox, 1, 0)
        grid.addWidget(self.fromSpinBox, 1, 1)
        grid.addWidget(self.toComboBox, 2, 0)
        grid.addWidget(self.toLabel, 2, 1)
        self.setLayout(grid)

        self.fromComboBox.currentIndexChanged.connect(self.updateUi)
        self.toComboBox.currentIndexChanged.connect(self.updateUi)
        self.fromSpinBox.valueChanged.connect(self.updateUi)

    def updateUi(self):
            to = self.toComboBox.currentText()
            from_ = self.fromComboBox.currentText()
            amount = (self.rates[from_] / self.rates[to]) * self.fromSpinBox.value()
            self.toLabel.setText("%0.2f" % amount)

    def getdata(self): # Idea taken from the Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                if not line or line.startswith(b"#") or line.startswith(b"Closing "):
                    continue
                fields = line.split(b", ")
                if line.startswith(b"Date "):
                    date = fields[-1].decode('ascii')
                else:
                    try:
                        value = float(fields[-1].decode('ascii'))
                        self.rates[fields[0].decode('ascii')] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + str(date)
        except Exception as e:
            return "Failed to download:\n%s" % e
app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
