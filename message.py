import sys, sip, html
from PyQt4 import QtCore, QtGui 
#from pybirchMdiV4 import Ui_PyBirch
from IrcConnection import IrcConnection
from ServerOutputSorter import ServerOutputSorter
from pybirchMessage import Ui_BirchMessageWindow
from userInputSorter import UserInputSorter
from TextString import TextString
from NickListView import NickListView
from time import strftime

from struct import unpack
import string

try:
    from PyQt4.QtCore import QString
except ImportError:
    QString = str

class Message(QtGui.QMdiSubWindow):
	_channel = ""
	_nick = ""

	__version__ = "Message v. 0.1"	

	def __init__(self, my_channel,my_config, parent=None):
		
		self._channel=my_channel
		self._nick=""
		self.config=my_config

		#print "DEBUG-------->In Channel :"+_channel_

		QtGui.QMdiSubWindow.__init__(self,parent)

		sip.delete(self.layout())

		self.ui = Ui_BirchSubWindow()

		self.ui.setupUi(self)

#		self.ui.setupUi(self)
		
		self.ui.label_ChanName.setText(self._channel)
	
		self.setWindowTitle(self._channel)


		#install the key event filter.
		self.ui.text_input.installEventFilter(self)
		
		#Why on God's Green was this EVER set to True? 
		self.ui.editor_Window.setOverwriteMode(False)
		
		self.tabSearchString=""
		self.tabSearchIndex=0

	def get_channel_name(self):
	
		return self._channel


	def append_channel_text(self,myString):
		myQString = QString(str(myString))
		#self.ui.editor_Window.append(myQString)
		try:
			showTime=self.config.get("Channel_Settings", "Time")
		except:
			self.config.add_section("Channel_Settings")
			self.config.set("Channel_Settings","Time", "True")
			showTime="True"
		
		if showTime=="True":
			current_time = strftime("%H:%M")
			myQString="["+current_time+"] "+myQString
		
		#myQString = cgi.escape(myQString)

		#Move the cursor. 
		#self.ui.editor_Window.moveCursor(11,False)
		#self.ui.editor_Window.insertHtml(myQString+"<br>")

		#This apparently does what I expect it to do, AND moves the
		#scrollbars appropriately. I'm sure I've tried this before, but it didn't work,
		#Now it does. So, I'm leaving it like this
		self.ui.editor_Window.append(myQString)		

		#self.ui.editor_Window.moveCursor(11,False)
		
		del myQString
		


	def eventFilter(self, obj ,event):
		if event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.InsertParagraphSeparator):
		       # self.sendToServer()
			self.process_input_event()

		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Space:
			self.tabSearchString = ""
			self.tabSearchIndex=0
	
		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
			self.process_tab_event()

			
			return True

		return False

	def process_tab_event(self):
		
		print("Processing Tab Event")
		
		originalString = self.ui.text_input.text()
		
		#searchString = str(originalString.rsplit(None, 1))
		searchString = originalString.split(" ")[-1]
		
		print("<DEBUG>:channel.process_tab_event():"+searchString)
		#Search string stored for repeated searches.
		if(self.tabSearchString == ""):
			self.tabSearchString=searchString
			self.tabSearchIndex=0
		else:
			self.tabSearchIndex=self.tabSearchIndex+1
			
		resultString = self._nicklist.search_nick(self.tabSearchString, self.tabSearchIndex)
		
		
		if resultString != "":
			#originalString=originalString.rsplit(" ", 1)[0]
			
			if originalString.endswith(searchString):
				originalString= originalString[:-len(searchString)]
			
			#originalString = originalString.rstrip(searchString)
			
			if len(originalString) == 0:
				self.ui.text_input.setText(originalString +resultString)
			else:
				self.ui.text_input.setText(originalString+resultString)
				#self.ui.text_input.setText(originalString +" "+ resultString)
		else:
			originalString=originalString[:-len(searchString)]
			self.ui.text_input.setText(originalString+self.tabSearchString)
			
			self.tabSearchIndex=0
			self.tabSearchString=""


	def process_input_event(self):


		channelName=self._channel

		originalString = self.ui.text_input.text()

		textToSend = originalString
		displayText = textToSend

		uIS = UserInputSorter()

		ts = uIS.process_input(channelName, self._nick, originalString)
		#self.ui.editor_Window.moveCursor(11,False)
#
#		myTextToSwitch = textToSend.split(" ")
#
#		if myTextToSwitch[0][0:1] == "/":
#			if myTextToSwitch[0] == "/msg":
#			        #Note, this doesn't in any way work.
#				remainderIndex = textToSend.find(myTextToSwitch[1])
#				textToSend = "PRIVMSG "+myTextToSwitch[1]+" "+textToSend[remainderIndex:]
#				displayText = "**Messaging "+myTextToSwitch[1]+textToSend[remainderIndex:]
#			else:
#				textToSend = str(textToSend[1:])
#				displayText = "---"+str(textToSend). 
#remainderIndex=string.find(strServerOutput,":",2)
#		else:
#			textToSend = "PRIVMSG "+channelName+" :"+textToSend
#			displayText = "["+_nick_+"] "+originalString

		try:
			showTime=self.config.get("Channel_Settings", "Time")
		except:
			pass


		self.emit(QtCore.SIGNAL("UserInput"),ts.get_original_string())
		
		myDisplayString = ts.get_display_string()
		
		if showTime == "True":
			current_time = strftime("%H:%M")
			myDisplayString="["+current_time+"] "+myDisplayString
		
		myDisplayString = html.escape(myDisplayString)
		
	#	self.ui.editor_Window.insertHtml(myDisplayString+"<br>")
		self.ui.editor_Window.append(myDisplayString)
		self.ui.text_input.setText("")
		
		#Search String for tab-searches reset to empty.
		self.tabSearchIndex=0
		self.tabSearchString=""


	def nick_update(self, my_new_nick):
		
		self._nick = my_new_nick


	def closeEvent(self, closeEvent):

		self.emit(QtCore.SIGNAL("Channel_Closed"),self._channel)
		#del(self._button)
		self._button.deleteLater();
		closeEvent.accept();


###
# While insert_nick currently works, the listWidget will need a QAbstractView in order to be able to remove
# items. This will deal with @, +, and other standard modifiers of the channel. definately TODO!
###
	def insert_nick(self, ts):
		#this is being done this way for future proofing
		print ("<DEBUG>Channel.py:insert_nick", ts.get_message())
		for myNick in ts.get_message().split():
			myNickToAdd = myNick.replace(":","",1 )
			self._nicklist.insert_nick(myNickToAdd)
		#	self.ui.listWidget.addItem(QtGui.QListWidgetItem(myNickToAdd))
		
		
	def remove_nick(self, ts):
		
		print("<DEBUG>Channel.py:remove_nick"+self._channel+" :"+ts.get_nick())
		for myNick in ts.get_nick().split():
			myNickToRemove = myNick.replace(":", "", 1)
			found = self._nicklist.remove_nick(myNickToRemove)
		#	self.ui.listWidget.removeItemWidget(QtGui.QListWidgetItem(myNickToRemove))
		if(found):
			self.append_channel_text(ts.get_display_string())

	def nicklist_update(self, ts):
		
		print("[Debug]:Channel:nicklist_update"+ts.get_nick()+"->"+ts.get_mode_user())
		
		self._nicklist.update_nick(ts.get_nick(), ts.get_mode_user())
		
		
		
		
	def nick_mode_change(self, ts):
		self._nicklist.changeStatus(ts.get_mode_user(), ts.get_mode_settings())

	def button_click(self):
		#sender = self.sender
		if self.isMinimized():
			self.show()
			self.showNormal()
		else:
			self.showMinimized()
			self.hide()
	
	def set_button(self, button):
		self._button = button
		self._button.resize(250, 150)
		
	def get_button (self):
		return self._button
