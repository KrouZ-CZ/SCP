# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SCP.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import random, time

def animate():
    a = 0
    while a <= 100:
        ui.progressBar.setValue(a)
        time.sleep(0.01)
        a += 1
def wt(w):
    sg = QMessageBox()
    sg.resize(100, 100)
    if w == 'w':
        te = 'Вы выиграли!'
    elif w == 'p':
        te = 'Вы проиграли'
    else:
        te = 'Ничья'

    sg.setWindowTitle('Результат')
    sg.setText(str(te))

    x = sg.exec_()
def pr(x, win):
    if win == 'S':
        if x == 0:
            wt = 'n'
        elif x == 1:
            wt = 'w'
        else:
            wt = 'p'
    if win == 'C':
        if x == 0:
            wt = 'p'
        elif x == 1:
            wt = 'n'
        else:
            wt = 'w'
    if win == 'P':
        if x == 0:
            wt = 'w'
        elif x == 1:
            wt = 'p'
        else:
            wt = 'n'
    return wt
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(396, 257)
        self.S = QtWidgets.QPushButton(Form)
        self.S.setGeometry(QtCore.QRect(70, 180, 75, 71))
        self.S.setObjectName("pushButton")
        self.C = QtWidgets.QPushButton(Form)
        self.C.setGeometry(QtCore.QRect(160, 180, 75, 71))
        self.C.setObjectName("pushButton_2")
        self.P = QtWidgets.QPushButton(Form)
        self.P.setGeometry(QtCore.QRect(250, 180, 75, 71))
        self.P.setObjectName("pushButton_3")
        self.ME = QtWidgets.QPushButton(Form)
        self.ME.setGeometry(QtCore.QRect(320, 10, 75, 31))
        self.ME.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 120, 211, 31))
        self.label.setStyleSheet("font-size: 25px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 70, 211, 31))
        self.label_2.setStyleSheet("font-size: 25px;")
        self.label_2.setObjectName("label_2")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(10, 10, 301, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Камень, ножницы, бумага!"))
        self.S.setText(_translate("Form", "Камень"))
        self.C.setText(_translate("Form", "Ножницы"))
        self.P.setText(_translate("Form", "Бумага"))
        self.ME.setText(_translate("Form", "О нас"))
        self.label.setText(_translate("Form", "Бот:"))
        self.label_2.setText(_translate("Form", "Вы:"))

def start(winh):
    ui.label.setText("Бот: ")
    winb = ['Камень', 'Ножницы', 'Бумага']
    x = random.randint(0, 2)
    bot = winb[x]
    win = pr(x, winh)
    if winh == 'S':
        winh = 'Камень'
    elif winh == 'C':
        winh = 'Ножницы'
    else:
        winh = 'Бумага'
    ui.label_2.setText("Вы: " + winh)
    animate()
    ui.label.setText("Бот: " + bot)
    wt(win)


def ME():
    msg = QMessageBox()
    msg.setWindowTitle('О нас')
    msg.setText("Мы, компания @Kvant`s studios\nЯвляемся разработчиками игры:\nКамень, ножницы, бумага.\nДля связи с нами пишите на почту \nили в ВК:\n\nkvantgd@gmail.com\nvk.com/kvantgd")

    x = msg.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    ui.S.clicked.connect( lambda: start("S") )
    ui.C.clicked.connect( lambda: start("C") )
    ui.P.clicked.connect( lambda: start("P") )
    ui.ME.clicked.connect( ME )

    sys.exit(app.exec_())
