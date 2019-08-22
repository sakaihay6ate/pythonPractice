# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(561, 594)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(300, 0, 256, 571))
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 80, 51, 16))
        self.label.setObjectName("label")
        self.symbolWidth = QtWidgets.QLineEdit(Form)
        self.symbolWidth.setGeometry(QtCore.QRect(90, 80, 113, 20))
        self.symbolWidth.setObjectName("symbolWidth")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 110, 51, 16))
        self.label_2.setObjectName("label_2")
        self.symbolHeight = QtWidgets.QLineEdit(Form)
        self.symbolHeight.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.symbolHeight.setObjectName("symbolHeight")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 140, 61, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 170, 61, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 200, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 230, 31, 16))
        self.label_6.setObjectName("label_6")
        self.initxPos = QtWidgets.QLineEdit(Form)
        self.initxPos.setGeometry(QtCore.QRect(90, 140, 113, 20))
        self.initxPos.setObjectName("initxPos")
        self.inityPos = QtWidgets.QLineEdit(Form)
        self.inityPos.setGeometry(QtCore.QRect(90, 170, 113, 20))
        self.inityPos.setObjectName("inityPos")
        self.col = QtWidgets.QLineEdit(Form)
        self.col.setGeometry(QtCore.QRect(90, 200, 113, 20))
        self.col.setObjectName("col")
        self.row = QtWidgets.QLineEdit(Form)
        self.row.setGeometry(QtCore.QRect(90, 230, 113, 20))
        self.row.setObjectName("row")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQtPractice"))
        self.pushButton.setText(_translate("Form", "計算"))
        self.label.setText(_translate("Form", "圖騰寬:"))
        self.label_2.setText(_translate("Form", "圖騰高:"))
        self.label_3.setText(_translate("Form", "起始x座標"))
        self.label_4.setText(_translate("Form", "起始y座標"))
        self.label_5.setText(_translate("Form", "行數"))
        self.label_6.setText(_translate("Form", "列數"))
