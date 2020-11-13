# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchMessage.ui'
#
# Created: Sat Feb 22 20:59:07 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_BirchMessageWindow(object):
    def setupUi(self, BirchMessageWindow):
        BirchMessageWindow.setObjectName(_fromUtf8("BirchMessageWindow"))
        BirchMessageWindow.resize(549, 324)
        self.gridLayout = QtWidgets.QGridLayout(BirchMessageWindow)
        self.gridLayout.setContentsMargins(2, 4, 2, 2)
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.editor_Window = QtWidgets.QTextEdit(BirchMessageWindow)
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.gridLayout.addWidget(self.editor_Window, 0, 0, 1, 2)
        self.frame = QtWidgets.QFrame(BirchMessageWindow)
        self.frame.setMinimumSize(QtCore.QSize(0, 0))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(2)
#        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.text_input = QtWidgets.QLineEdit(self.frame)
        self.text_input.setObjectName(_fromUtf8("text_input"))
        self.horizontalLayout.addWidget(self.text_input)
        self.label_ChanName = QtWidgets.QLabel(self.frame)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.horizontalLayout.addWidget(self.label_ChanName)
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)
        self.gridLayout.setColumnStretch(0, 100)

        self.retranslateUi(BirchMessageWindow)
        QtCore.QMetaObject.connectSlotsByName(BirchMessageWindow)

    def retranslateUi(self, BirchMessageWindow):
        BirchMessageWindow.setWindowTitle(_translate("BirchMessageWindow", "Form", None))
        self.label_ChanName.setText(_translate("BirchMessageWindow", "(None)", None))

