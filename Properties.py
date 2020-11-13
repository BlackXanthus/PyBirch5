import sys, os
import configparser


#GUI imports
from PyQt5 import QtCore, QtGui
from pyqt5_Properties_ui import Ui_Dialog
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget



class Properties(QWidget):
	
	dict_DefaultConfig = dict()

	def __init__(self,parent=None):
	
		QWidget.__init__(self, parent)
		self.config = configparser.ConfigParser(allow_no_value=True)
		self.setupDefaultConfigArray()
		
		try:
			if os.path.isfile("py-birch.cfg"):
				self.config.read("py-birch.cfg")
		except:
			print("<DEBUG> Unable to open Config File")
			

	def show_window(self, parent=None):
		QWidget.__init__(self,parent)
		#self.config=my_config
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		
		#Fill Values
		self.ui.input_Server.setText(self.get("IRC_Server", "Server"))
		self.ui.input_Nickname.setText(self.get("IRC_Server","Nickname"))
		self.ui.input_Port.setText(self.get("IRC_Server","Port"))
		self.ui.input_RealName.setText(self.get("IRC_Server","RealName"))
		self.ui.input_Ident.setText(self.get("IRC_Server","Ident"))
		self.ui.input_BackupNick.setText(self.get("IRC_Server","BackupNick"))
		self.ui.input_FontSize.setText(self.get("Font", "Size"))
		self.ui.fontComboBox.setCurrentFont(QFont(self.get("Font","Name")))
		
		self.show()
		
		#QtCore.QObject.connect(self.ui.buttonBox,QtCore.SIGNAL("accepted()"),self.save_Preferences)

	def save_Preferences(self):
		
		print("<Properties_DEBUG>Saving Properties")
		try:
			with open('py-birch.cfg', 'w') as configfile:
				self.config.write(configfile)
		except:
			print("<Properties_DEBUG> Config Writing Fail")

	def get(self, propSection, propKey):
		
		configValue=""

		try:
			configValue=self.config.get(propSection, propKey)
		except:
			configValue=self.dict_DefaultConfig[propSection][propKey]

		return configValue
			
	def set(self, propSection, propKey,  propValue):

		if(not self.config.has_section(propSection)):
			self.config.add_section(propSection)

		#if(not self.config.has_option(propSection,propKey)):
			#self.config.add_option(propSection,propKey)

		try:
			 self.config.set(propSection,propKey,propValue)
		except:
			print("<Properties_DEBUG>"+propSection+","+propKey+","+propValue+" - could not be added")

	#####
	# This holds the default array. 
	# 
	# The theory being that whatever the program calls,
	# this holds an answer.
	def setupDefaultConfigArray(self):
		
		self.dict_DefaultConfig= dict()

		#Text Settings
		self.dict_DefaultConfig["Font"] = dict()
		self.dict_DefaultConfig["Font"]["Name"] = "Arial"
		self.dict_DefaultConfig["Font"]["Size"] = "5"

		#Colour Settings
		self.dict_DefaultConfig["Text_Colours"] = dict()
		self.dict_DefaultConfig["Text_Colours"]["Action"] = "Blue"
		self.dict_DefaultConfig["Text_Colours"]["Mode"] = "Red"
		self.dict_DefaultConfig["Text_Colours"]["Join"] = "Green"
		self.dict_DefaultConfig["Text_Colours"]["Part"] = "Green"
		self.dict_DefaultConfig["Text_Colours"]["Quit"] = "Lime"
		self.dict_DefaultConfig["Text_Colours"]["Kick"] = "Tomato"
		self.dict_DefaultConfig["Text_Colours"]["Message"] = "Blue"
		self.dict_DefaultConfig["Text_Colours"]["Attention"] = "Orange"
		self.dict_DefaultConfig["Text_Colours"]["Notice"] = "Purple"

		#Channel Settings
		self.dict_DefaultConfig["Channel_Settings"] = dict()
		self.dict_DefaultConfig["Channel_Settings"]["Time"]= "True"
		self.dict_DefaultConfig["Channel_Settings"]["Button_Alert_Colour"] = "red"
		self.dict_DefaultConfig["Channel_Settings"]["Nickcomplete_Postscript"]=":"
		self.dict_DefaultConfig["Channel_Settings"]["ShowNicknameOnWindow"]="False"
		self.dict_DefaultConfig["Channel_Settings"]["ShowChanNameOnTitleBar"]="False"

		#Status Window Settings
		self.dict_DefaultConfig["Status_Settings"] = dict()
		self.dict_DefaultConfig["Status_Settings"]["Button_Alert_Activated"] = "False"
		self.dict_DefaultConfig["Status_Settings"]["ShowNicknameOnWindow"]="True"

		#Server Seettings
		self.dict_DefaultConfig["IRC_Server"] = dict()
		self.dict_DefaultConfig["IRC_Server"]["Server"]= "irc.dal.net"
		self.dict_DefaultConfig["IRC_Server"]["Nickname"]="PyBirch1"
		self.dict_DefaultConfig["IRC_Server"]["Port"]="6667"
		self.dict_DefaultConfig["IRC_Server"]["RealName"]="Birch Python Client"
		self.dict_DefaultConfig["IRC_Server"]["Ident"]="PyBirch"
		self.dict_DefaultConfig["IRC_Server"]["BackupNick"]="PyBirch2"

                #Nickname Settings
		self.dict_DefaultConfig["Nickname"]=dict()
		self.dict_DefaultConfig["Nickname"]["HostDisplay"]="False"

	def accept(self):
		
		#update config.
		if(self.ui.input_Server.text()!=""):
			self.set("IRC_Server","Server", self.ui.input_Server.text())
			print("<DEBUG:Properties>Sever Set")
		if(self.ui.input_Nickname.text()!=""):
			self.set("IRC_Server", "Nickname", self.ui.input_Nickname.text())
			print("<DEBUG:Properties> Nickname Set")
		if(self.ui.input_Port.text()!=""):
			self.set("IRC_Server","Port",self.ui.input_Port.text())
		if(self.ui.input_BackupNick.text()!=""):
			self.set("IRC_Server","BackupNick",self.ui.input_BackupNick.text())
		if(self.ui.input_RealName.text()!=""):
			self.set("IRC_Server","RealName",self.ui.input_RealName.text())
		if(self.ui.input_Ident.text()!=""):
			self.set("IRC_Server","Ident",self.ui.input_Ident.text())
		if(self.ui.input_FontSize.text()!=""):
			self.set("Font", "Size", self.ui.input_FontSize.text())
		if(self.ui.fontComboBox.currentText()!=""):
			self.set("Font", "Name", self.ui.fontComboBox.currentText())

		self.saveConfig()
		self.hide()

	def reject(self):
		print("Properties: Reject")
		self.hide()
	
	def saveConfig(self):
		
		try:
			with open('py-birch.cfg', 'w') as configfile:
				self.config.write(configfile)
		except IOError as err:
			print (err)
		except OSError as err:
			print (err)
		except configparser.Error as err:
			print(err)
		except configparser.ParseError as err:
			print(err)
		except:
			print(err)
			print("Config Writing Fail - Properties")
