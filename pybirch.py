# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirch.ui'
#
# Created: Sun Aug 26 22:58:31 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_PyBirch(object):
    def setupUi(self, PyBirch):
        PyBirch.setObjectName(_fromUtf8("PyBirch"))
        PyBirch.resize(800, 600)
        self.centralwidget = QtGui.QWidget(PyBirch)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.button_Open = QtGui.QPushButton(self.centralwidget)
        self.button_Open.setObjectName(_fromUtf8("button_Open"))
        self.gridLayout.addWidget(self.button_Open, 0, 0, 1, 1)
        self.editor_Window = QtGui.QTextEdit(self.centralwidget)
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.gridLayout.addWidget(self.editor_Window, 1, 0, 1, 4)
        self.text_Input = QtGui.QLineEdit(self.centralwidget)
        self.text_Input.setObjectName(_fromUtf8("text_Input"))
        self.gridLayout.addWidget(self.text_Input, 2, 1, 1, 2)
        self.button_Send = QtGui.QPushButton(self.centralwidget)
        self.button_Send.setObjectName(_fromUtf8("button_Send"))
        self.gridLayout.addWidget(self.button_Send, 2, 3, 1, 1)
        self.label_ChanName = QtGui.QLabel(self.centralwidget)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.gridLayout.addWidget(self.label_ChanName, 2, 0, 1, 1)
        self.button_Disconnect = QtGui.QPushButton(self.centralwidget)
        self.button_Disconnect.setObjectName(_fromUtf8("button_Disconnect"))
        self.gridLayout.addWidget(self.button_Disconnect, 0, 3, 1, 1)
        PyBirch.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyBirch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        PyBirch.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyBirch)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyBirch.setStatusBar(self.statusbar)

        self.retranslateUi(PyBirch)
        QtCore.QMetaObject.connectSlotsByName(PyBirch)

    def retranslateUi(self, PyBirch):
        PyBirch.setWindowTitle(QtGui.QApplication.translate("PyBirch", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Open.setText(QtGui.QApplication.translate("PyBirch", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Send.setText(QtGui.QApplication.translate("PyBirch", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ChanName.setText(QtGui.QApplication.translate("PyBirch", "(none)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Disconnect.setText(QtGui.QApplication.translate("PyBirch", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))

