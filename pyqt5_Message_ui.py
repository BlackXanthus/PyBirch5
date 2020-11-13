# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt5_Message.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_BirchMessageWindow(object):
    def setupUi(self, BirchMessageWindow):
        BirchMessageWindow.setObjectName("BirchMessageWindow")
        BirchMessageWindow.resize(549, 324)
        self.gridLayout = QtWidgets.QGridLayout(BirchMessageWindow)
        self.gridLayout.setContentsMargins(0, 1, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.editor_Window = QtWidgets.QTextEdit(BirchMessageWindow)
        self.editor_Window.setObjectName("editor_Window")
        self.gridLayout.addWidget(self.editor_Window, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(BirchMessageWindow)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.text_input = QtWidgets.QLineEdit(self.frame)
        self.text_input.setObjectName("text_input")
        self.horizontalLayout.addWidget(self.text_input)
        self.label_ChanName = QtWidgets.QLabel(self.frame)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName("label_ChanName")
        self.horizontalLayout.addWidget(self.label_ChanName)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 100)

        self.retranslateUi(BirchMessageWindow)
        QtCore.QMetaObject.connectSlotsByName(BirchMessageWindow)

    def retranslateUi(self, BirchMessageWindow):
        _translate = QtCore.QCoreApplication.translate
        BirchMessageWindow.setWindowTitle(_translate("BirchMessageWindow", "Form"))
        self.label_ChanName.setText(_translate("BirchMessageWindow", "(None)"))

