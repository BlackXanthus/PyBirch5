# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Properties.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 419)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setObjectName("tabWidget")
        self.IRCServer = QtWidgets.QWidget()
        self.IRCServer.setObjectName("IRCServer")
        self.formLayout = QtWidgets.QFormLayout(self.IRCServer)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.IRCServer)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.input_Nickname = QtWidgets.QLineEdit(self.IRCServer)
        self.input_Nickname.setText("")
        self.input_Nickname.setObjectName("input_Nickname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.input_Nickname)
        self.label_3 = QtWidgets.QLabel(self.IRCServer)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.input_Server = QtWidgets.QLineEdit(self.IRCServer)
        self.input_Server.setObjectName("input_Server")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.input_Server)
        self.label_4 = QtWidgets.QLabel(self.IRCServer)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.input_Port = QtWidgets.QLineEdit(self.IRCServer)
        self.input_Port.setObjectName("input_Port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.input_Port)
        self.input_RealName = QtWidgets.QLineEdit(self.IRCServer)
        self.input_RealName.setObjectName("input_RealName")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.input_RealName)
        self.lineEdit = QtWidgets.QLineEdit(self.IRCServer)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(self.IRCServer)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.IRCServer)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.IRCServer)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.input_BackupNick = QtWidgets.QLineEdit(self.IRCServer)
        self.input_BackupNick.setObjectName("input_BackupNick")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.input_BackupNick)
        self.tabWidget.addTab(self.IRCServer, "")
        self.Font = QtWidgets.QWidget()
        self.Font.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Font.setObjectName("Font")
        self.formLayout_2 = QtWidgets.QFormLayout(self.Font)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.Font)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fontComboBox = QtWidgets.QFontComboBox(self.Font)
        self.fontComboBox.setObjectName("fontComboBox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fontComboBox)
        self.label_8 = QtWidgets.QLabel(self.Font)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.Font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.tabWidget.addTab(self.Font, "")
        self.TextColours = QtWidgets.QWidget()
        self.TextColours.setObjectName("TextColours")
        self.formLayout_3 = QtWidgets.QFormLayout(self.TextColours)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_9 = QtWidgets.QLabel(self.TextColours)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.butn_TextActionColour = QtWidgets.QPushButton(self.TextColours)
        self.butn_TextActionColour.setObjectName("butn_TextActionColour")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.butn_TextActionColour)
        self.tabWidget.addTab(self.TextColours, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Nickname"))
        self.label_3.setText(_translate("Dialog", "Server"))
        self.label_4.setText(_translate("Dialog", "Port"))
        self.label_5.setText(_translate("Dialog", "Real Name"))
        self.label_6.setText(_translate("Dialog", "Ident"))
        self.label_7.setText(_translate("Dialog", "Backup Nick"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.IRCServer), _translate("Dialog", "IRC Server"))
        self.label.setText(_translate("Dialog", "Font Name"))
        self.label_8.setText(_translate("Dialog", "Font Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Font), _translate("Dialog", "Font"))
        self.label_9.setText(_translate("Dialog", "Text Action Color"))
        self.butn_TextActionColour.setText(_translate("Dialog", "Open Colour Picker"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TextColours), _translate("Dialog", "Text Colours"))

