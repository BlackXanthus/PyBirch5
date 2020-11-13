# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchProperties.ui'
#
# Created: Fri Dec  5 01:28:23 2014
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(389, 175)
        self.formLayout = QtGui.QFormLayout(Dialog)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.lbl_ServerName = QtGui.QLabel(Dialog)
        self.lbl_ServerName.setObjectName(_fromUtf8("lbl_ServerName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.lbl_ServerName)
        self.txt_ServerName = QtGui.QLineEdit(Dialog)
        self.txt_ServerName.setObjectName(_fromUtf8("txt_ServerName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.txt_ServerName)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.lbl_NickName = QtGui.QLabel(Dialog)
        self.lbl_NickName.setObjectName(_fromUtf8("lbl_NickName"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lbl_NickName)
        self.txt_Nickname = QtGui.QLineEdit(Dialog)
        self.txt_Nickname.setObjectName(_fromUtf8("txt_Nickname"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.txt_Nickname)
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label)
        self.fontComboBox = QtGui.QFontComboBox(Dialog)
        self.fontComboBox.setObjectName(_fromUtf8("fontComboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.fontComboBox)
        self.lbl_FontSize = QtGui.QLabel(Dialog)
        self.lbl_FontSize.setObjectName(_fromUtf8("lbl_FontSize"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.lbl_FontSize)
        self.txt_FontSize = QtGui.QLineEdit(Dialog)
        self.txt_FontSize.setObjectName(_fromUtf8("txt_FontSize"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txt_FontSize)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.lbl_ServerName.setText(_translate("Dialog", "Server Name", None))
        self.lbl_NickName.setText(_translate("Dialog", "Nick Name", None))
        self.label.setText(_translate("Dialog", "Font Name", None))
        self.lbl_FontSize.setText(_translate("Dialog", "Font Size", None))

