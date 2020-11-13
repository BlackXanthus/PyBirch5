# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchChannelV1.ui'
#
# Created: Tue May  7 22:39:09 2013
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
        BirchSubWindow.resize(660, 460)
        self.gridLayout = QtGui.QGridLayout(BirchSubWindow)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(BirchSubWindow)
        self.frame.setMaximumSize(QtCore.QSize(16777172, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.text_input = QtGui.QLineEdit(self.frame)
        self.text_input.setObjectName(_fromUtf8("text_input"))
        self.horizontalLayout.addWidget(self.text_input)
        self.label_ChanName = QtGui.QLabel(self.frame)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.horizontalLayout.addWidget(self.label_ChanName)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtGui.QFrame(BirchSubWindow)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtGui.QSplitter(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.editor_Window = QtGui.QTextEdit(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editor_Window.sizePolicy().hasHeightForWidth())
        self.editor_Window.setSizePolicy(sizePolicy)
        self.editor_Window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editor_Window.setReadOnly(True)
        self.editor_Window.setAcceptRichText(True)
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.list_NickList = QtGui.QListView(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_NickList.sizePolicy().hasHeightForWidth())
        self.list_NickList.setSizePolicy(sizePolicy)
        self.list_NickList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.list_NickList.setObjectName(_fromUtf8("list_NickList"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)

        self.retranslateUi(BirchSubWindow)
        QtCore.QMetaObject.connectSlotsByName(BirchSubWindow)

    def retranslateUi(self, BirchSubWindow):
        BirchSubWindow.setWindowTitle(QtGui.QApplication.translate("BirchSubWindow", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label_ChanName.setText(QtGui.QApplication.translate("BirchSubWindow", "(None)", None, QtGui.QApplication.UnicodeUTF8))

