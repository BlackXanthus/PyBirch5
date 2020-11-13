# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchMdiV4.ui'
#
# Created: Sun Sep 15 21:01:10 2013
#      by: PyQt4 UI code generator 4.10
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
        self.button_Tile = QtGui.QPushButton(self.frame)
        self.button_Tile.setObjectName(_fromUtf8("button_Tile"))
        self.horizontalLayout.addWidget(self.button_Tile)
        self.button_Cascade = QtGui.QPushButton(self.frame)
        self.button_Cascade.setObjectName(_fromUtf8("button_Cascade"))
        self.horizontalLayout.addWidget(self.button_Cascade)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.gridLayout.addWidget(self.mdiArea, 1, 0, 1, 1)
        self.button_bar = QtGui.QFrame(self.centralwidget)
        self.button_bar.setMinimumSize(QtCore.QSize(0, 29))
        self.button_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_bar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.button_bar.setFrameShadow(QtGui.QFrame.Raised)
        self.button_bar.setObjectName(_fromUtf8("button_bar"))
        self.button_bar_layout = QtGui.QHBoxLayout(self.button_bar)
        self.button_bar_layout.setSpacing(1)
        self.button_bar_layout.setContentsMargins(1, 2, -1, 2)
        self.button_bar_layout.setObjectName(_fromUtf8("button_bar_layout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.button_bar_layout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.button_bar, 2, 0, 1, 1)
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
        self.menuWindows = QtGui.QMenu(self.menubar)
        self.menuWindows.setObjectName(_fromUtf8("menuWindows"))
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
        self.actionCascade = QtGui.QAction(PyBirch)
        self.actionCascade.setObjectName(_fromUtf8("actionCascade"))
        self.actionTile = QtGui.QAction(PyBirch)
        self.actionTile.setObjectName(_fromUtf8("actionTile"))
        self.menuServer.addAction(self.actionConnect)
        self.menuServer.addAction(self.actionDisconnect)
        self.menuConfiguration.addAction(self.actionProperties)
        self.menuHelp.addAction(self.actionAbout_Py_Birch)
        self.menuWindows.addAction(self.actionCascade)
        self.menuWindows.addAction(self.actionTile)
        self.menubar.addAction(self.menuServer.menuAction())
        self.menubar.addAction(self.menuConfiguration.menuAction())
        self.menubar.addAction(self.menuWindows.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(PyBirch)
        QtCore.QMetaObject.connectSlotsByName(PyBirch)

    def retranslateUi(self, PyBirch):
        PyBirch.setWindowTitle(_translate("PyBirch", "MainWindow", None))
        self.button_Connect.setText(_translate("PyBirch", "Connect", None))
        self.button_Disconnect.setText(_translate("PyBirch", "Disconnect", None))
        self.button_Properties.setText(_translate("PyBirch", "Properties", None))
        self.button_Tile.setToolTip(_translate("PyBirch", "Tile Windows", None))
        self.button_Tile.setText(_translate("PyBirch", "Tile Windows", None))
        self.button_Cascade.setToolTip(_translate("PyBirch", "Cascade Windows", None))
        self.button_Cascade.setText(_translate("PyBirch", "Cascade Windows", None))
        self.menuServer.setTitle(_translate("PyBirch", "Server", None))
        self.menuConfiguration.setTitle(_translate("PyBirch", "Configuration", None))
        self.menuHelp.setTitle(_translate("PyBirch", "Help", None))
        self.menuWindows.setTitle(_translate("PyBirch", "Windows", None))
        self.actionConnect.setText(_translate("PyBirch", "Connect", None))
        self.actionDisconnect.setText(_translate("PyBirch", "Disconnect", None))
        self.actionProperties.setText(_translate("PyBirch", "Properties", None))
        self.actionAbout_Py_Birch.setText(_translate("PyBirch", "About Py-Birch", None))
        self.actionCascade.setText(_translate("PyBirch", "Cascade", None))
        self.actionTile.setText(_translate("PyBirch", "Tile", None))

