import sys, sip, html,copy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
#from pybirchMdiV4 import Ui_PyBirch
from IrcConnection import IrcConnection
from ServerOutputSorter import ServerOutputSorter
#from pybirchChannelV4 import Ui_BirchSubWindow
from pyqt5_ChannelV4_ui import Ui_BirchSubWindow
from pyqt5_Message_ui import Ui_BirchMessageWindow
from userInputSorter import UserInputSorter
from TextString import TextString
from NickListView import NickListView
from time import strftime

from struct import unpack
import string

try:
    from PyQt5.QtCore import QStrin
except ImportError:
    QString = str

class Channel(QtWidgets.QMdiSubWindow):

	CHANNEL=1
	MESSAGE=2
	STATUS=3
	_channel = ""
	_nick = ""

	_commandList = []
	_commandListCopy = []
	_commandListSize=0

	__version__ = "Channel v. 0.3"	
	_button = ""
	_buttonBackground="background-color: None"
	
	plugins=""
	
	#PyQt5 Signals
	UserInput = QtCore.pyqtSignal(str)
	Channel_Closed = QtCore.pyqtSignal(str)

	#So that the background doesn't get permanently set to the
	#Alert colour, this flip is used. 
	_minimised=False

	def __init__(self, my_channel,my_config,my_plugins, myChannelType=1,parent=None):
		
		self._channel=my_channel
		self._nick=""
		self.config=my_config
		self.channelType = myChannelType
		self.plugins=my_plugins
		
		#print "DEBUG-------->In Channel :"+_channel_

		QtWidgets.QMdiSubWindow.__init__(self,parent)

		sip.delete(self.layout())

		if self.channelType == self.MESSAGE or self.channelType == self.STATUS:
			self.ui = Ui_BirchMessageWindow()
		else:
			self.ui = Ui_BirchSubWindow()

		self.ui.setupUi(self)

		if self.channelType==self.STATUS:
			if(self._nick != ""):
				self.ui.label_ChanName.setText(self._nick +"-"+self._channel)
			else:
				self.ui.label_ChanName.setText(self._channel)
		else:
			self.ui.label_ChanName.setText(self._channel)	


		self.set_channel_title(self._channel)
		#self.setWindowTitle(self._channel)


		#install the key event filter.
		self.ui.text_input.installEventFilter(self)

		#font ssize should probably not be done like this
		tempFontSize = self.config.get("Font","Size")
		fontSize= tempFontSize.replace("pt", "")

		self.ui.text_input.setFont(QFont(self.config.get("Font","Name"), int(fontSize)))

		self._nicklist = NickListView()

		if self.channelType == self.CHANNEL:
			self.ui.list_NickList.setModel(self._nicklist)
			sizesList = []
			sizesList.append(600)
			sizesList.append(200)
			self.ui.splitter.setSizes(sizesList)


			self.ui.list_NickList.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
			#self.ui.list_NickList.customContextMenuRequested.connect(self.popup)


		#Why on God's Green was this EVER set to True?
		#And why does this not work on Message Windows? 
		self.ui.editor_Window.setOverwriteMode(False)
		self.ui.editor_Window.setReadOnly(True)

		
		self.tabSearchString=""
		self.tabSearchIndex=0

		self._commandList = []
		self._commandListCopy = []
		self._commandListSize=0

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

	def set_channel_title(self,myTitle):

		if (self.channelType==self.STATUS):
			#set to myTitle, in case I ever get round to changing
			#to the server
			self.setWindowTitle(myTitle)
		else:		
			if(self.config.get("Channel_Settings","ShowChanNameOnTitleBar") == "True"): 
				self.setWindowTitle(self.get_channel_name()+" - "+myTitle)
			else:
				if(myTitle==""):
					self.setWindowTitle(self.get_channel_name())
				else:
					self.setWindowTitle(myTitle)

	
		#self.setWindowTitle(self.get_channel_name()+" - "+myTitle)
		#Tooltip removed due to being irritating. 
		#self.setToolTip(myTitle)


	##############
	# Mouse Commands
	#############
	def contextMenuEvent(self,event):
		menu=QtWidgets.QMenu()

		MyNickname=""
		selected=""

		#selected=self.ui.list_NickList.clicked		
		selectedIndexes= self.ui.list_NickList.selectedIndexes()
		if len(selectedIndexes)==0:
			print("<DEBUG>Channel:NickList: Did you click on the nicklist?")
		else:
			mySelected=selectedIndexes[0]
			selected=mySelected.data(QtCore.Qt.EditRole)
			myNickClass = self._nicklist.search_nick_class(selected)
			myNickname=myNickClass
			print("<DEBUG>Channel:NickList:"+selected)		
			print("<DEBUG>Channel:Nicklist:Host: "+myNickClass.get_host())


		#selected=self.ui.list_NickList.indexAt(event.pos())
		#myIndex=self.ui.list_NickList.currentItem().text()
		#myIndex=self._nicklist.data(selected,QtCore.Qt.DisplayRole)
		#myIndex=self.ui.list_NickList.itemAt(event.pos())	
		#Remember that myIndex includes andy channel status atm.	
		contextMenuName=QtWidgets.QAction(selected,self)

		menu.addAction(contextMenuName)

		menu.addSeparator()
		contextMenuKick=QtWidgets.QAction("Kick "+selected,self)
		contextMenuKick.triggered.connect(lambda:self.kick(myNickname))
		menu.addAction(contextMenuKick)


		contextMenuBan=QtWidgets.QAction("Ban "+selected,self)	
		contextMenuBan.triggered.connect(lambda:self.ban(myNickname))
		menu.addAction(contextMenuBan)


		contextMenuVoice=QtWidgets.QAction("Voice "+selected,self)
	#	contextMenuVoice.triggered.connect(lambda:self.whois(selected))
		contextMenuVoice.triggered.connect(lambda:self.voice(myNickname))
		menu.addAction(contextMenuVoice)

		contextMenuWhois=QtWidgets.QAction("Who is "+selected,self)
		contextMenuWhois.triggered.connect(lambda:self.whois(selected))
		#contextMenuWhois.connect("activate",lambda:self.whois(selected))
		menu.addAction(contextMenuWhois)

		menu.exec_(event.globalPos())

	#def contextMenuName(self)

	def whois(self,user):
		print("<DEBUG>Channel:whois: whois "+user)
		#use the inbuilt process system (for now!)
		#process_intput_event("/whois "+user)
		#self.emit(QtCore.SIGNAL("UserInput"),"whois "+user)
		self.UserInput.emit("whois "+user)

	def kick(self,user):
		print("<DEUBG>Channel:Kick:Kick "+user.get_nickname())
		self.UserInput.emit("kick "+self.get_channel_name()+" "+user.get_nickname())
		
	def voice(self,user):
		print("<DEUBG>Channel:Voice:Voice "+user.get_nickname())
		self.UserInput.emit("mode "+self.get_channel_name()+" +v "+user.get_nickname())
	
	def ban(self,user):
		print("<DEBUG>Channel:Mode:Ban "+user.get_nickname()+" "+user.get_host())

	
	
	def append_channel_ts(self, myTs):
		#do stuff with updating of the nicklist
		print("<DEBUG>Channels:append_channel_ts:"+myTs.get_nickname_class().get_host())

		if self.get_channel_type() == self.CHANNEL:
			try:
				if(self._nicklist.search_nick_class(myTs.get_nick())!=""):
					print("<DEBUG>Channels:append_channel_ts2:"+myTs.get_nickname_class().get_host())
					self._nicklist.update_host(myTs.get_nick(), myTs.get_nickname_class())	
			except KeyError as e:
					print("KeyError Updating Hostname for:"+myTs.get_nick()+" - "+ e.args[0]+e.args[1])

		#self._commandList.append(myTs.get_display_string())
		self.append_channel_text(myTs.get_display_string())

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
		
		
		if self.windowState() == QtCore.Qt.WindowMinimized:
			if not self._minimised:
				self._buttonBackground=self._button.styleSheet()

				button_alert=self.config.get("Channel_Settings","Button_Alert_Colour")


				##
				#This aweful code is to make sure that
				#you can turn notifications off based on
				#channel type. 
				#
				#Though currently it's only Status that 
				#you can turn off.
				##
				if(self.channelType==self.STATUS):
					if(self.config.get("Status_Settings","Button_Alert_Activated")=="True"):
						self._button.setStyleSheet("background-color: "+button_alert)
				if(self.channelType==self.CHANNEL):
					self._button.setStyleSheet("background-color: "+button_alert)

				if(self.channelType==self.MESSAGE):
					self._button.setStyleSheet("background-color: "+button_alert)

				self._minimised=True
		
		#myQString="<font face=\""+self.config.get("Font", "Name")+"\" size=\""+self.config.get("Font","Size")+"\">"+myQString+"</font>"
		####
		# using CSS gives a much better control of the font size, rather than html size. 
		# it does mean, however, needing to add "px" after the size in the size box. 
		myQString="<span style=\"font-family:"+self.config.get("Font","Name")+"; font-size:"+self.config.get("Font", "Size")+";\">"+myQString+"</span>"
		#myQString = cgi.escape(myQString)

		#Move the cursor. 
		#self.ui.editor_Window.moveCursor(11,False)
		#self.ui.editor_Window.insertHtml(myQString+"<br>")

		#This apparently does what I expect it to do, AND moves the
		#scrollbars appropriately. I'm sure I've tried this before, but it didn't work,
		#Now it does. So, I'm leaving it like this
		#print ("[DEBUG] "+self._channel+" append_channel "+myQString)

		self.ui.editor_Window.append(myQString)		

		#self.ui.editor_Window.moveCursor(11,False)
		
		del myQString


	def changeEvent(self, event):
		if event.type() == QtCore.QEvent.WindowStateChange:
			if self.windowState() == QtCore.Qt.NoModifier:
				print("Window Has no modifier")
			if self.windowState() == QtCore.Qt.WindowMinimized:
				print("Minimising window...")
				if not self.isMinimized():
					self.showMinimized()
					self.hide()
					self.setWindowState(QtCore.Qt.WindowMinimized)
					print("Channels:Debug:WindowMinimised Event")
					self._minimised=True
	
			elif event.oldState() & QtCore.Qt.WindowMinimized:
				print("Changing Button Style Sheet")	
				self._button.setStyleSheet(self._buttonBackground)
				self._minimised=False
	

	#self.scrollArea
	#verticalScrollBar -> setValue (verticalScrollBar -> minimum()) (or maximum()).


#		if event.type() ==QtCore.QEvent

	def eventFilter(self, obj ,event):
		if event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.InsertParagraphSeparator):
		       # self.sendToServer()
			self.process_input_event()

		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Space:
			self.tabSearchString = ""
			self.tabSearchIndex=0
	
		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Tab:
			if(self.channelType==self.CHANNEL):
				self.process_tab_event()
			
			return True
			
		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Up:
			self.process_command_list_event(event)

		if event.type() == QtCore.QEvent.KeyPress and event.key() == QtCore.Qt.Key_Down:
			self.process_command_list_event(event)
			
			

		return False
	


	def process_command_list_event(self,event):
		
		if(event.key() == QtCore.Qt.Key_Up):
			try:
				#because length size starts at 1, and List starts at 0
				self._commandListSize = self._commandListSize-1
				#If the value is less than 0, give a blank line, then restart
				if(self._commandListSize < 0):
					self._commandListSize=len(self._commandList)
					popString=""
				else:
					popString = self._commandListCopy[self._commandListSize]
				#popString = self._commandListCopy.pop()
				print(popString)
				self.ui.text_input.setText(popString)
			except IndexError:
				print("Out of Elements")
				self._commandListSize=len(self._commandList)
				self.ui.text_input.setText("")

		if(event.key() == QtCore.Qt.Key_Down):
			try:
				#because length size starts at 1, and List starts at 0
				self._commandListSize = self._commandListSize+1
				if(self._commandListSize > len(self._commandList)):
					self._commandListSize=len(self._commandList)
					popString=""
				else:
					popString = self._commandListCopy[self._commandListSize]
				
				#popString = self._commandListCopy.pop()
				print(popString)
				self.ui.text_input.setText(popString)
			except IndexError:
				print("Out of Elements")
				self._commandListSize=0
				self.ui.text_input.setText("")

				
		print("processing command list event")

	def process_tab_event(self):

		print("Processing Tab Event")
		postscript=self.config.get("Channel_Settings","Nickcomplete_Postscript")
		
		originalString = self.ui.text_input.text()
			
		#searchString = str(originalString.rsplit(None, 1))
		if (originalString.endswith(postscript)):
			orignalString = originalString[:-len(postscript)]
			searchString = originalString.split(" ")[-1]
		else:
			searchString = originalString.split(" ")[-1]
		
		#print("<DEBUG>:channel.process_tab_event():"+searchString)
		#Search string stored for repeated searches.
		if(self.tabSearchString == ""):
			self.tabSearchString=searchString
			self.tabSearchIndex=0
		else:
			#Here, we check to make sure the user hasn't
			#changed who they wish to talk too.
			if(originalString.lower().startswith(self.tabSearchString.lower())):
				self.tabSearchIndex=self.tabSearchIndex+1
			else:
				#if they are not the same, it's a new search.
				self.tabSearchString=searchString
				self.tabSearchIndex=0
			
		resultString = self._nicklist.search_nick(self.tabSearchString, self.tabSearchIndex)
		
		
		if resultString != "":
			#originalString=originalString.rsplit(" ", 1)[0]
			postscript=self.config.get("Channel_Settings","Nickcomplete_Postscript")
			if originalString.endswith(searchString):
				originalString= originalString[:-len(searchString)]
			
			#originalString = originalString.rstrip(searchString)
			
			if len(originalString) == 0:

				#The final string has the postscript added.
				#makes for easier conversations
				self.ui.text_input.setText(originalString +resultString+postscript)
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
	
		#For the command list
		#We don't add empty strings to the list
		if(self.ui.text_input.text()!=""):
			self._commandList.append(self.ui.text_input.text())
			self._commandListCopy = copy.deepcopy(self._commandList)
			self._commandListSize = len(self._commandList)

		textToSend = originalString
		displayText = textToSend

		#I have no idea why I thought this was a good idea!		
		#originalString = html.escape(originalString)

		uIS = UserInputSorter()

		ts = uIS.process_input(channelName, self._nick, originalString,self.config,self.plugins)

		
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

#		try:
#			showTime=self.config.get("Channel_Settings", "Time")
#		except:
#			pass


		#self.emit(QtCore.SIGNAL("UserInput"),ts.get_original_string())
		self.UserInput.emit(ts.get_original_string())

		myDisplayString = ts.get_display_string()

#		if showTime == "True":
#			current_time = strftime("%H:%M")
#			myDisplayString="["+current_time+"] "+myDisplayString

	#	myDisplayString = cgi.escape(myDisplayString)

	#	self.ui.editor_Window.insertHtml(myDisplayString+"<br>")
		#Ensures that a single method is use for channel update.
		self.append_channel_text(myDisplayString)

		self.ui.text_input.setText("")

		#Search String for tab-searches reset to empty.
		self.tabSearchIndex=0
		self.tabSearchString=""


	def nick_update(self, my_new_nick):
		
		self._nick = my_new_nick
		#This needs to be an eventual option
		if self.channelType==self.STATUS:
			if(self.config.get("Status_Settings","ShowNicknameOnWindow") == "True"): 
				self.ui.label_ChanName.setText(self._nick+"-"+self._channel)
			else:
				self.ui.label_ChanName.setText(self._channel)
		else:
			if(self.config.get("Channel_Settings","ShowNicknameOnWindow") == "True"): 
				self.ui.label_ChanName.setText(self._nick +"-"+self._channel)
			else:
				self.ui.label_ChanName.setText(self._channel)

	def closeChannel(self):

		#We don't close the Status window. 
		#It dies when the program dies
		if not self.channelType== self.STATUS:
			#self.emit(QtCore.SIGNAL("Channel_Closed"),self._channel)
			self.Channel_Closed.emit(self._channel)
			#del(self._button)
			self._button.deleteLater()


	def closeEvent(self, closeEvent):

		print("Close Event Fired")
		
		if not self.channelType == self.STATUS:
			self.closeChannel()
		#	self.emit(QtCore.SIGNAL("Channel_Closed"),self._channel)
			#del(self._button)
			#self._button.deleteLater()
			closeEvent.accept()
		else:
			closeEvent.ignore()


###
# This works for multiple nicknames on channel join
# 
# However, we don't get hostnames for those when they join. 
# This might mean that we need a way of updating the host in the list
# some other way.
#
# When someone messages the channel, we are given their hostname.
# If we produce a quick 'check hostname' method, then these will be filled
# out as people chat. This does mean that the quiet ones remain without a
# hostname, but that's probably better than whoising the entire channel on 
# join. 
##

	def insert_multiple_nicks(self, ts):
		#this is being done this way for future proofing
		if self.channelType==self.CHANNEL:
			print ("<DEBUG>Channel.py:insert_nick", ts.get_message())
			for myNick in ts.get_message().split():
				myNick=myNick.strip()
				myNickToAdd = myNick.replace(":","",1 )
				self._nicklist.insert_nick(myNickToAdd)
		#	self.ui.listWidget.addItem(QtGui.QListWidgetItem(myNickToAdd))

	#This works for adding a host to people who join the channel
	#Now we just need a way of testing a speaker's host, and updating it
	def insert_nick(self, ts):
		#this is being done this way for future proofing
		if self.channelType==self.CHANNEL:
			print ("<DEBUG>Channel.py:insert_nick", ts.get_message())
			print("<DEBUG>Channel:insert_nick:Len Nicks:"+str(len(ts.get_message().split())))
			if(len(ts.get_message().split()) > 1):
				for myNick in ts.get_message().split():
					myNick=myNick.strip()
					myNickToAdd = myNick.replace(":","",1 )
					self._nicklist.insert_nick_multiple(myNickToAdd)
		#	self.ui.listWidget.addItem(QtGui.QListWidgetItem(myNickToAdd))
			else:
				self._nicklist.insert_nick_single(ts)
				


		
	def remove_nick(self, ts):

		found = False
		if not self.channelType == self.MESSAGE:
			print("<DEBUG>Channel.py:remove_nick- Channel - "+self._channel+" : nick - "+ts.get_nick())
			for myNick in ts.get_nick().split():
				myNick=myNick.strip()
				myNickToRemove = myNick.replace(":", "", 1)
				found = self._nicklist.remove_nick(myNickToRemove)
		return found
			#removed because it's unnecessary.
			#self.ui.listWidget.removeItemWidget(QtGui.QListWidgetItem(myNickToRemove))

		#This is seemingly causing the message to appear in the same channel twice. 
		#	if(found):
		#		self.append_channel_text(ts.get_display_string()+"remove_nick")
		#		print("<DEBUG>FOUND. Channel.py:remove_nick- Channel - "+self._channel+" : nick - "+ts.get_nick())

	def nicklist_update(self, ts):

		if not self.channelType == self.MESSAGE:	
			print("[Debug]:Channel:nicklist_update:"+self.get_channel_name()+":"+ts.get_nick()+"->"+ts.get_mode_user())
			ts.set_nick(ts.get_nick().strip())	
			found = self._nicklist.update_nick(ts.get_nick(), ts.get_mode_user())

			if found:
				self.append_channel_text (ts.get_display_string())
			else:
				print("<DEBUG>Channel:nick_update:Nickname"+ts.get_nick()+" not found on "+self.get_channel_name())
				
		
	def nick_mode_change(self, ts):

		if not self.channelType == self.MESSAGE:
			print("[DEBUG]:Channel:nick_mode_change "+ts.get_mode_user()+">"+ts.get_mode_settings())
			ts.set_mode_user(ts.get_mode_user().strip())
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

	def get_channel_type(self):
		return self.channelType


	def resizeEvent(self, E):
		super().resizeEvent(E)
		self.ui.editor_Window.verticalScrollBar().setValue(self.ui.editor_Window.verticalScrollBar().maximum())
