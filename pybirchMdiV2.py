# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchMdiV2.ui'
#
# Created: Fri Jan 25 16:36:06 2013
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
        PyBirch.resize(798, 646)
        self.centralwidget = QtGui.QWidget(PyBirch)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.button_Connect = QtGui.QPushButton(self.frame)
        self.button_Connect.setObjectName(_fromUtf8("button_Connect"))
        self.horizontalLayout.addWidget(self.button_Connect)
        self.button_Disconnect = QtGui.QPushButton(self.frame)
        self.button_Disconnect.setObjectName(_fromUtf8("button_Disconnect"))
        self.horizontalLayout.addWidget(self.button_Disconnect)
        self.button_Properties = QtGui.QPushButton(self.frame)
        self.button_Properties.setObjectName(_fromUtf8("button_Properties"))
        self.horizontalLayout.addWidget(self.button_Properties)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        brush = QtGui.QBrush(QtGui.QColor(227, 224, 176))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
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
        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 1)
        PyBirch.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(PyBirch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuServer = QtGui.QMenu(self.menubar)
        self.menuServer.setObjectName(_fromUtf8("menuServer"))
        self.menuConfiguration = QtGui.QMenu(self.menubar)
        self.menuConfiguration.setObjectName(_fromUtf8("menuConfiguration"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        PyBirch.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(PyBirch)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        PyBirch.setStatusBar(self.statusbar)
        self.actionConnect = QtGui.QAction(PyBirch)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionDisconnect = QtGui.QAction(PyBirch)
        self.actionDisconnect.setObjectName(_fromUtf8("actionDisconnect"))
        self.actionProperties = QtGui.QAction(PyBirch)
        self.actionProperties.setObjectName(_fromUtf8("actionProperties"))
        self.actionAbout_Py_Birch = QtGui.QAction(PyBirch)
        self.actionAbout_Py_Birch.setObjectName(_fromUtf8("actionAbout_Py_Birch"))
        self.menuServer.addAction(self.actionConnect)
        self.menuServer.addAction(self.actionDisconnect)
        self.menuConfiguration.addAction(self.actionProperties)
        self.menuHelp.addAction(self.actionAbout_Py_Birch)
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PyBirch)
        QtCore.QMetaObject.connectSlotsByName(PyBirch)

    def retranslateUi(self, PyBirch):
        PyBirch.setWindowTitle(QtGui.QApplication.translate("PyBirch", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Connect.setText(QtGui.QApplication.translate("PyBirch", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Disconnect.setText(QtGui.QApplication.translate("PyBirch", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.button_Properties.setText(QtGui.QApplication.translate("PyBirch", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.Status.setWindowTitle(QtGui.QApplication.translate("PyBirch", "Subwindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ChanName.setText(QtGui.QApplication.translate("PyBirch", "(None)", None, QtGui.QApplication.UnicodeUTF8))
        self.menuServer.setTitle(QtGui.QApplication.translate("PyBirch", "Server", None, QtGui.QApplication.UnicodeUTF8))
        self.menuConfiguration.setTitle(QtGui.QApplication.translate("PyBirch", "Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("PyBirch", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConnect.setText(QtGui.QApplication.translate("PyBirch", "Connect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDisconnect.setText(QtGui.QApplication.translate("PyBirch", "Disconnect", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProperties.setText(QtGui.QApplication.translate("PyBirch", "Properties", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Py_Birch.setText(QtGui.QApplication.translate("PyBirch", "About Py-Birch", None, QtGui.QApplication.UnicodeUTF8))

