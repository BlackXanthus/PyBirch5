# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchMdiV5.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PyBirch(object):
    def setupUi(self, PyBirch):
        PyBirch.setObjectName("PyBirch")
        PyBirch.resize(655, 518)
        self.centralwidget = QtWidgets.QWidget(PyBirch)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(2, 1, 2, 1)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName("gridLayout")
        self.button_bar = QtWidgets.QFrame(self.centralwidget)
        self.button_bar.setMinimumSize(QtCore.QSize(0, 29))
        self.button_bar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.button_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.button_bar.setObjectName("button_bar")
        self.button_bar_layout = QtWidgets.QHBoxLayout(self.button_bar)
        self.button_bar_layout.setContentsMargins(1, 2, -1, 2)
        self.button_bar_layout.setSpacing(1)
        self.button_bar_layout.setObjectName("button_bar_layout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.button_bar_layout.addItem(spacerItem)
        self.gridLayout.addWidget(self.button_bar, 3, 0, 1, 1)
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        brush = QtGui.QBrush(QtGui.QColor(239, 239, 119))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.mdiArea.setBackground(brush)
        self.mdiArea.setTabsClosable(False)
        self.mdiArea.setTabsMovable(False)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_Connect = QtWidgets.QPushButton(self.frame)
        self.button_Connect.setObjectName("button_Connect")
        self.horizontalLayout.addWidget(self.button_Connect)
        self.button_Disconnect = QtWidgets.QPushButton(self.frame)
        self.button_Disconnect.setObjectName("button_Disconnect")
        self.horizontalLayout.addWidget(self.button_Disconnect)
        self.button_Properties = QtWidgets.QPushButton(self.frame)
        self.button_Properties.setObjectName("button_Properties")
        self.horizontalLayout.addWidget(self.button_Properties)
        self.button_Tile = QtWidgets.QPushButton(self.frame)
        self.button_Tile.setObjectName("button_Tile")
        self.horizontalLayout.addWidget(self.button_Tile)
        self.button_Cascade = QtWidgets.QPushButton(self.frame)
        self.button_Cascade.setObjectName("button_Cascade")
        self.horizontalLayout.addWidget(self.button_Cascade)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        PyBirch.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(PyBirch)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 655, 20))
        self.menubar.setObjectName("menubar")
        self.menuServer = QtWidgets.QMenu(self.menubar)
        self.menuServer.setObjectName("menuServer")
        self.menuConfiguration = QtWidgets.QMenu(self.menubar)
        self.menuConfiguration.setObjectName("menuConfiguration")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuWindows = QtWidgets.QMenu(self.menubar)
        self.menuWindows.setObjectName("menuWindows")
        PyBirch.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(PyBirch)
        self.statusbar.setObjectName("statusbar")
        PyBirch.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(PyBirch)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(PyBirch)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionProperties = QtWidgets.QAction(PyBirch)
        self.actionProperties.setObjectName("actionProperties")
        self.actionAbout_Py_Birch = QtWidgets.QAction(PyBirch)
        self.actionAbout_Py_Birch.setObjectName("actionAbout_Py_Birch")
        self.actionCascade = QtWidgets.QAction(PyBirch)
        self.actionCascade.setObjectName("actionCascade")
        self.actionTile = QtWidgets.QAction(PyBirch)
        self.actionTile.setObjectName("actionTile")
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
        _translate = QtCore.QCoreApplication.translate
        PyBirch.setWindowTitle(_translate("PyBirch", "MainWindow"))
        self.button_Connect.setText(_translate("PyBirch", "Connect"))
        self.button_Disconnect.setText(_translate("PyBirch", "Disconnect"))
        self.button_Properties.setText(_translate("PyBirch", "Properties"))
        self.button_Tile.setToolTip(_translate("PyBirch", "Tile Windows"))
        self.button_Tile.setText(_translate("PyBirch", "Tile Windows"))
        self.button_Cascade.setToolTip(_translate("PyBirch", "Cascade Windows"))
        self.button_Cascade.setText(_translate("PyBirch", "Cascade Windows"))
        self.menuServer.setTitle(_translate("PyBirch", "Server"))
        self.menuConfiguration.setTitle(_translate("PyBirch", "Configuration"))
        self.menuHelp.setTitle(_translate("PyBirch", "Help"))
        self.menuWindows.setTitle(_translate("PyBirch", "Windows"))
        self.actionConnect.setText(_translate("PyBirch", "Connect"))
        self.actionDisconnect.setText(_translate("PyBirch", "Disconnect"))
        self.actionProperties.setText(_translate("PyBirch", "Properties"))
        self.actionAbout_Py_Birch.setText(_translate("PyBirch", "About Py-Birch"))
        self.actionCascade.setText(_translate("PyBirch", "Cascade"))
        self.actionTile.setText(_translate("PyBirch", "Tile"))
