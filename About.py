import sys,os
import configparser

#GUI Imports
from PyQt5 import QtCore, QtGui
from pyqt5_About_ui import Ui_About
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QDialog, QWidget


class About(QDialog):

	def __init(self,parent=None):
		QWidget.__init__(self,parent)

	def show_window(self,parent=None):
		QDialog.__init__(self,parent)

		self.ui = Ui_About()
		self.ui.setupUi(self)

		mySource=open('todo.txt').read()


		#self.connect(self.ui.Close,QtCore.SIGNAL("clicked()"), self.closeButton) 
		self.ui.Close.clicked.connect(self.closeButton)

		
		self.ui.inputText.setPlainText(mySource)
	
		self.show()


	def closeButton(self):
		self.hide()
		self.destroy()		

	def closeEvent(self, closeEvent):
	
		self.hide()
		closeEvent.accept()
		self.destroy()		
