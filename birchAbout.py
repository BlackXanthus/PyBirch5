# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchAbout.ui'
#
# Created: Sat Nov 14 20:42:22 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(461, 446)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.input = QtGui.QTextBrowser(Dialog)
        self.input.setObjectName(_fromUtf8("input"))
        self.verticalLayout.addWidget(self.input)
        self.Close = QtGui.QPushButton(Dialog)
        self.Close.setObjectName(_fromUtf8("Close"))
        self.verticalLayout.addWidget(self.Close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Close.setText(_translate("Dialog", "Close", None))

