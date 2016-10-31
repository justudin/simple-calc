"""
    Title: Simple Calc GUI
    Written by: justudin
    Url:  http://github.com/justudin/simple-calc
    This is simple calc app written in Python by using PyQt5
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QLabel, QLineEdit

# Cacl_GUI Class
class Calc_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # lbl num1
        lblnum1 = QLabel('Input 1', self)
        lblnum1.move(15, 10)
        # lbl num2
        lblnum2 = QLabel('Input 2', self)
        lblnum2.move(15, 50)
        # lbl result
        lblres = QLabel('Result', self)
        lblres.move(15, 200)
        # TextEdit for input1
        self.input1 = QLineEdit(self)
        self.input1.move(100, 10)
        # TextEdit for input2
        self.input2 = QLineEdit(self)
        self.input2.move(100, 50)
        # TextEdit for Result
        self.res = QLineEdit(self)
        self.res.move(100, 200)
        # Button for +
        btnplus = QPushButton("+", self)
        btnplus.move(30, 100)
        # Button for -
        btnminus = QPushButton("-", self)
        btnminus.move(150, 100)
        # Button for *
        btnmul = QPushButton("*", self)
        btnmul.move(30, 150)
        # Button for /
        btndiv = QPushButton("/", self)
        btndiv.move(150, 150)
        # button handler
        btnplus.clicked.connect(self.add)
        btnminus.clicked.connect(self.minus)
        btnmul.clicked.connect(self.mul)
        btndiv.clicked.connect(self.div)
        #statusBar
        self.statusBar().showMessage('Written by Udin')
        self.setGeometry(500, 500, 270, 270)
        self.setWindowTitle('Simple Calculator')
        self.show()
    # func for add
    def add(self):
        sender = self.sender()
        tot = float(self.input1.text())+float(self.input2.text())
        self.statusBar().showMessage('Written by Udin: button '+sender.text() + ' was pressed')
        self.res.setText(str(tot))
    # func for minus
    def minus(self):
        sender = self.sender()
        tot = float(self.input1.text())-float(self.input2.text())
        self.statusBar().showMessage('Written by Udin: button '+sender.text() + ' was pressed')
        self.res.setText(str(tot))
    # func for multiply
    def mul(self):
        sender = self.sender()
        tot = float(self.input1.text())*float(self.input2.text())
        self.statusBar().showMessage('Written by Udin: button '+ sender.text() + ' was pressed')
        self.res.setText(str(tot))
    # func for division
    def div(self):
        sender = self.sender()
        if (float(self.input2.text())==0):
            self.res.setText('divide by 0')
        else:
            tot = float(self.input1.text())/float(self.input2.text())
            self.statusBar().showMessage('Written by Udin: button '+sender.text() + ' was pressed')
            self.res.setText(str(tot))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calc_GUI()
    sys.exit(app.exec_())

