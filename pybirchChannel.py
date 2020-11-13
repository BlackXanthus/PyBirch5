# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchChannel.ui'
#
# Created: Thu Jan 24 10:22:42 2013
#      by: PyQt4 UI code generator 4.9.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_BirchSubWindow(object):
    def setupUi(self, BirchSubWindow):
        BirchSubWindow.setObjectName(_fromUtf8("BirchSubWindow"))
        BirchSubWindow.resize(660, 361)
        self.gridLayout = QtGui.QGridLayout(BirchSubWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor_Window = QtGui.QTextEdit(BirchSubWindow)
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.gridLayout.addWidget(self.editor_Window, 0, 0, 1, 3)
        self.text_input = QtGui.QLineEdit(BirchSubWindow)
        self.text_input.setObjectName(_fromUtf8("text_input"))
        self.gridLayout.addWidget(self.text_input, 1, 0, 1, 3)
        self.label_ChanName = QtGui.QLabel(BirchSubWindow)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.gridLayout.addWidget(self.label_ChanName, 1, 3, 1, 1)
        self.list_NickList = QtGui.QListView(BirchSubWindow)
        self.list_NickList.setObjectName(_fromUtf8("list_NickList"))
        self.gridLayout.addWidget(self.list_NickList, 0, 3, 1, 1)
        self.gridLayout.setColumnMinimumWidth(0, 100)
        self.gridLayout.setColumnMinimumWidth(3, 50)
        self.gridLayout.setColumnStretch(0, 100)
        self.gridLayout.setColumnStretch(3, 50)

        self.retranslateUi(BirchSubWindow)
        QtCore.QMetaObject.connectSlotsByName(BirchSubWindow)

    def retranslateUi(self, BirchSubWindow):
        BirchSubWindow.setWindowTitle(QtGui.QApplication.translate("BirchSubWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ChanName.setText(QtGui.QApplication.translate("BirchSubWindow", "(None)", None, QtGui.QApplication.UnicodeUTF8))

#from qmdisubwindow import QMdiSubWindow
