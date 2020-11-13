# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pybirchChannelV4.ui'
#
# Created: Wed Nov 11 22:58:35 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui,QtWidgets

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

class Ui_BirchSubWindow(object):
    def setupUi(self, BirchSubWindow):
        BirchSubWindow.setObjectName(_fromUtf8("BirchSubWindow"))
        BirchSubWindow.resize(632, 331)
        self.gridLayout = QtWidgets.QGridLayout(BirchSubWindow)
        #self.gridLayout.setMargin(3)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtWidgets.QFrame(BirchSubWindow)
        self.frame.setMaximumSize(QtCore.QSize(16777172, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        # self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.text_input = QtWidgets.QLineEdit(self.frame)
        self.text_input.setObjectName(_fromUtf8("text_input"))
        self.horizontalLayout.addWidget(self.text_input)
        self.label_ChanName = QtWidgets.QLabel(self.frame)
        self.label_ChanName.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ChanName.setObjectName(_fromUtf8("label_ChanName"))
        self.horizontalLayout.addWidget(self.label_ChanName)
        self.gridLayout.addWidget(self.frame, 2, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(BirchSubWindow)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        #self.horizontalLayout_2.setMargin(3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.editor_Window = QtWidgets.QTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editor_Window.sizePolicy().hasHeightForWidth())
        self.editor_Window.setSizePolicy(sizePolicy)
        self.editor_Window.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.editor_Window.setAcceptDrops(False)
        self.editor_Window.setTabChangesFocus(False)
        self.editor_Window.setDocumentTitle(_fromUtf8(""))
        self.editor_Window.setUndoRedoEnabled(False)
        self.editor_Window.setReadOnly(True)
        self.editor_Window.setOverwriteMode(False)
        self.editor_Window.setAcceptRichText(True)
        self.editor_Window.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.editor_Window.setObjectName(_fromUtf8("editor_Window"))
        self.list_NickList = QtWidgets.QListView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_NickList.sizePolicy().hasHeightForWidth())
        self.list_NickList.setSizePolicy(sizePolicy)
        self.list_NickList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.list_NickList.setObjectName(_fromUtf8("list_NickList"))
        self.horizontalLayout_2.addWidget(self.splitter)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(BirchSubWindow)
        QtCore.QMetaObject.connectSlotsByName(BirchSubWindow)

    def retranslateUi(self, BirchSubWindow):
        BirchSubWindow.setWindowTitle(_translate("BirchSubWindow", "Form", None))
        self.label_ChanName.setText(_translate("BirchSubWindow", "(None)", None))

