# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchAbout.ui'
#
# Created: Sat Nov 14 21:33:53 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

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

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName(_fromUtf8("About"))
        About.resize(748, 424)
        self.verticalLayout = QtGui.QVBoxLayout(About)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.inputText = QtGui.QTextBrowser(About)
        self.inputText.setObjectName(_fromUtf8("inputText"))
        self.verticalLayout.addWidget(self.inputText)
        self.Close = QtGui.QPushButton(About)
        self.Close.setObjectName(_fromUtf8("Close"))
        self.verticalLayout.addWidget(self.Close)

        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(_translate("About", "Dialog", None))
        self.Close.setText(_translate("About", "Close", None))

