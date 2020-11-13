
####
#Made reduntant in Alpha 0.4
#
# As this provided no extra functionality from the Channel, and is, in essance,
# simply a speciall channel, various additions were made to Channel.py
# To perform the same function. This has meant less duplication of code. 
####
import sys, sip
from PyQt5 import QtCore, QtGui 
#from pybirchMdiV4 import Ui_PyBirch
#from IrcConnection import IrcConnection
#from ServerOutputSorter import ServerOutputSorter
from pybirchMessage import Ui_BirchMessageWindow
from userInputSorter import UserInputSorter
from TextString import TextString
from NickListView import NickListView
from time import strftime

from struct import unpack
import string

try:
    from PyQt5.QtCore import QString
except ImportError:
    QString = str

class StatusWindow(QtGui.QMdiSubWindow):

	_channel = ""
	_nick = ""
	_button = ""

	__version__ = "Status v. 0.1"	
		

	def __init__(self, my_channel, parent=None):
		
		self._channel=my_channel
		self._nick=""
		#Config will need to be passed in later, because of the order of
		#creation.
		#self.config=my_config
		
		#print "DEBUG-------->In Channel :"+_channel_

		QtGui.QMdiSubWindow.__init__(self,parent)

		sip.delete(self.layout())

		self.ui = Ui_BirchMessageWindow()

		self.ui.setupUi(self)

#		self.ui.setupUi(self)
		
		self.ui.label_ChanName.setText(self._channel)
	
		self.setWindowTitle(self._channel)


		#install the key event filter.
		self.ui.text_input.installEventFilter(self)
		
		#self._nicklist = NickListView()
		#self.ui.list_NickList.setModel(self._nicklist)


	#	self.ui.setWindowTitle(_channel_)
	
	#Quick and Dirty hashing method.	
	#--- May have problems with similarly-named channels. eg
	# test, tset, ttse and so on. MUST TEST (v0.1)
	#http://bytes.com/topic/python/answers/23620-string-ascii-values
      #  def __hash__(self):
#		global _channel_
#		return unpack('%sB' % len(value), value)

	def get_channel_name(self):
	
		return self._channel


	def append_channel_text(self,myString):
		myQString = QString(str(myString))
		showTime = "True"
		#self.ui.editor_Window.append(myQString)
		#try:
		#	showTime=self.config.get("Channel_Settings", "Time")
		#except:
		#	self.config.add_section("Channel_Settings")
		#	self.config.set("Channel_Settings","Time", "True")
		#	showTime="True"
		
		if showTime=="True":
			current_time = strftime("%H:%M")
			myQString="["+current_time+"] "+myQString
		
		self.ui.editor_Window.insertHtml(myQString+"<br>")

		#This should stop the window from updating when scrolling			#up and down through the channel!
#		if not self.ui.editor_Window.isHorizontalSliderPressed():

		self.ui.editor_Window.moveCursor(11,False)
		
		del myQString
		


	def eventFilter(self, obj ,event):
		if event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.InsertParagraphSeparator):
		       # self.sendToServer()
			self.process_input_event()
	
		
		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
			self.process_tab_event()
			
			return True

		return False

	def process_tab_event(self):
		
		print("Processing Tab Event")
		
		#originalString = self.ui.text_input.text()
		
		#searchString = str(originalString.rsplit(None, 1))
		#searchString = originalString.split(" ")[-1]
		
		#print(searchString)
		
		#resultString = self._nicklist.search_nick(searchString)
		
		#if resultString != "":
			#originalString=originalString.rsplit(" ", 1)[0]
			
			#if originalString.endswith(searchString):
		#		originalString= originalString[:-len(searchString)]
			
			#originalString = originalString.rstrip(searchString)
			
		#	if len(originalString) == 0:
		#		self.ui.text_input.setText(originalString +resultString)
		#	else:
		#		self.ui.text_input.setText(originalString +" "+ resultString)

	def process_input_event(self):


		channelName=self._channel

		originalString = self.ui.text_input.text()

		textToSend = originalString
		displayText = textToSend

		uIS = UserInputSorter()

		ts = uIS.process_input(channelName, self._nick, originalString)
		self.ui.editor_Window.moveCursor(11,False)
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
#				displayText = "---"+str(textToSend)
#remainderIndex=string.find(strServerOutput,":",2)
#		else:
#			textToSend = "PRIVMSG "+channelName+" :"+textToSend
#			displayText = "["+_nick_+"] "+originalString

		#try:
		#	showTime=self.config.get("Channel_Settings", "Time")
		#except:
		#	pass

		showTime = "True"


		self.emit(QtCore.SIGNAL("UserInput"),ts.get_original_string())
		
		myDisplayString = ts.get_display_string()
		
		if showTime == "True":
			current_time = strftime("%H:%M")
			myDisplayString="["+current_time+"] "+myDisplayString
			
		self.ui.editor_Window.insertHtml(myDisplayString+"<br>")
		self.ui.text_input.setText("")


	def nick_update(self, my_new_nick):
		
		self._nick = my_new_nick


	def closeEvent(self, closeEvent):

		self.emit(QtCore.SIGNAL("Channel_Closed"),self._channel)
		closeEvent.accept();
		print ("<StatusWindow : Close event> PANIC Mr Mannering!")

	def button_click(self):
		#sender = self.sender
		if self.isMinimized():
			self.show()
			self.showNormal()
		else:
			self.showMinimized()
			self.hide()

###
# While insert_nick currently works, the listWidget will need a QAbstractView in order to be able to remove
# items. This will deal with @, +, and other standard modifiers of the channel. definately TODO!
#
#	def insert_nick(self, ts):
#		#this is being done this way for future proofing
#		print ("<DEBUG>Channel.py:insert_nick", ts.get_message())
#		for myNick in ts.get_message().split():
#			myNickToAdd = myNick.replace(":","",1 )
#			self._nicklist.insert_nick(myNickToAdd)
		#	self.ui.listWidget.addItem(QtGui.QListWidgetItem(myNickToAdd))
		
		
#	def remove_nick(self, ts):
#		print("<DEBUG>Channel.py:remove_nick"+self._channel+" :"+ts.get_nick())
#		for myNick in ts.get_nick().split():
#			myNickToRemove = myNick.replace(":", "", 1)
#			found = self._nicklist.remove_nick(myNickToRemove)
		#	self.ui.listWidget.removeItemWidget(QtGui.QListWidgetItem(myNickToRemove))
#		if(found):
#			self.append_channel_text(ts.get_display_string())

#	def nick_mode_change(self, ts):
#		self._nicklist.changeStatus(ts.get_mode_user(), ts.get_mode_settings())
