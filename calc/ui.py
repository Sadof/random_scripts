# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(302, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 170, 61, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(10, 10, 281, 81))
        self.lcdNumber.setObjectName("lcdNumber")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 170, 61, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(150, 170, 61, 51))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 230, 61, 51))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(80, 230, 61, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 230, 61, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 290, 61, 51))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 290, 61, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 290, 61, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(80, 350, 61, 51))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(220, 170, 61, 51))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(220, 230, 61, 51))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_multi = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multi.setGeometry(QtCore.QRect(220, 290, 61, 51))
        self.pushButton_multi.setObjectName("pushButton_multi")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(220, 110, 61, 51))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.pushButton_div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_div.setGeometry(QtCore.QRect(220, 350, 61, 51))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_reset.setEnabled(True)
        self.pushButton_reset.setGeometry(QtCore.QRect(10, 110, 61, 51))
        self.pushButton_reset.setMouseTracking(False)
        self.pushButton_reset.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.pushButton_reset.setAutoRepeat(False)
        self.pushButton_reset.setAutoDefault(False)
        self.pushButton_reset.setDefault(False)
        self.pushButton_reset.setFlat(False)
        self.pushButton_reset.setObjectName("pushButton_reset")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(150, 350, 61, 51))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(150, 110, 61, 51))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_times.setGeometry(QtCore.QRect(80, 110, 61, 51))
        self.pushButton_times.setObjectName("pushButton_times")
        self.pushButton_negative = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_negative.setGeometry(QtCore.QRect(10, 350, 61, 51))
        self.pushButton_negative.setObjectName("pushButton_negative")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "7"))
        self.pushButton_8.setText(_translate("MainWindow", "8"))
        self.pushButton_9.setText(_translate("MainWindow", "9"))
        self.pushButton_4.setText(_translate("MainWindow", "4"))
        self.pushButton_5.setText(_translate("MainWindow", "5"))
        self.pushButton_6.setText(_translate("MainWindow", "6"))
        self.pushButton_1.setText(_translate("MainWindow", "1"))
        self.pushButton_2.setText(_translate("MainWindow", "2"))
        self.pushButton_3.setText(_translate("MainWindow", "3"))
        self.pushButton_0.setText(_translate("MainWindow", "0"))
        self.pushButton_plus.setText(_translate("MainWindow", "+"))
        self.pushButton_minus.setText(_translate("MainWindow", "-"))
        self.pushButton_multi.setText(_translate("MainWindow", "*"))
        self.pushButton_equal.setText(_translate("MainWindow", "="))
        self.pushButton_div.setText(_translate("MainWindow", "/"))
        self.pushButton_reset.setText(_translate("MainWindow", "C"))
        self.pushButton_10.setText(_translate("MainWindow", "."))
        self.pushButton_delete.setText(_translate("MainWindow", "←"))
        self.pushButton_times.setText(_translate("MainWindow", "^"))
        self.pushButton_negative.setText(_translate("MainWindow", "-"))


