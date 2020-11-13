# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchMdiV1.ui'
#
# Created: Sat Jun  9 20:02:17 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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
        self.button_Connect = QtGui.QPushButton(self.centralwidget)
        self.button_Connect.setObjectName(_fromUtf8("button_Connect"))
        self.gridLayout.addWidget(self.button_Connect, 0, 0, 1, 1)
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.Status = QtGui.QWidget()
        self.Status.setMinimumSize(QtCore.QSize(600, 400))
        self.Status.setFocusPolicy(QtCore.Qt.TabFocus)
        self.Status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Status.setAutoFillBackground(True)
        self.Status.setObjectName(_fromUtf8("Status"))
        self.editor_Window = QtGui.QTextEdit(self.Status)
        self.editor_Window.setGeometry(QtCore.QRect(0, 10, 601, 281))
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.text_Input = QtGui.QLineEdit(self.Status)
        self.text_Input.setGeometry(QtCore.QRect(130, 300, 471, 27))
        self.text_Input.setObjectName(_fromUtf8("text_Input"))
        self.label_ChanName = QtGui.QLabel(self.Status)
        self.label_ChanName.setGeometry(QtCore.QRect(10, 300, 101, 31))
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.gridLayout.addWidget(self.mdiArea, 14, 0, 1, 1)
        self.button_Disconnect = QtGui.QPushButton(self.centralwidget)
        self.button_Disconnect.setObjectName(_fromUtf8("button_Disconnect"))
        self.gridLayout.addWidget(self.button_Disconnect, 15, 0, 1, 1)
        PyBirch.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyBirch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        PyBirch.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyBirch)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyBirch.setStatusBar(self.statusbar)
        self.actionConnect = QtGui.QAction(PyBirch)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(PyBirch)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.menuServer.addAction(self.actionConnect)
        self.menuServer.addAction(self.actionDisconnect)
        self.menubar.addAction(self.menuServer.menuAction())

        self.retranslateUi(PyBirch)
        QtCore.QMetaObject.connectSlotsByName(PyBirch)

    def retranslateUi(self, PyBirch):
        PyBirch.setWindowTitle(QtGui.QApplication.translate("PyBirch", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Connect.setText(QtGui.QApplication.translate("PyBirch", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.Status.setWindowTitle(QtGui.QApplication.translate("PyBirch", "Subwindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ChanName.setText(QtGui.QApplication.translate("PyBirch", "(None)", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Disconnect.setText(QtGui.QApplication.translate("PyBirch", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.menuServer.setTitle(QtGui.QApplication.translate("PyBirch", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("PyBirch", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("PyBirch", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))

