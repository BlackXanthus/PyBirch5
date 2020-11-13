import sys, os, html

#GUI imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMdiSubWindow
from PyQt5.QtWidgets import QGridLayout
from pybirchMdiV5 import Ui_PyBirch
from pybirchMessage import Ui_BirchMessageWindow
#from StatusWindow import StatusWindow

#Client-Specific Class Imports. 
from IrcConnection import IrcConnection
from ServerOutputSorter import ServerOutputSorter
from Channel import Channel
from TextString import TextString
from Exceptions import Disconnected
from Properties import Properties 
from PluginArchitecture import PluginArchitecture
from About import About

import string, configparser

try:
    from PyQt5.QtCore import QString
except ImportError:
       # we are using Python3 so QString is not defined
       QString = str

class StartQT5(QMainWindow):

	global irc_Connection 
	#global server_OutputSorter
	global channelArray
	global channelWindow
	global _nick_
	global app

	const_NONE=0
	const_TILE=1
	const_CASCADE=2


	config=""
	_nick_=""
	_nick=""
	_version="0.5.0.1 ALPHA"
	statusWindow = ""
	_layout=const_NONE

	#PyQt5 Signals
	NickChange = QtCore.pyqtSignal(str)

	#Create and Empty array to hold the Channels in.
	channelArray=dict()


	def __init__(self,parent=None):
		global irc_Connection
		#global server_OutputSorter
		global channelWindow
		global _nick_

		#scan the plugins. 
		self.plugins=PluginArchitecture()

		QWidget.__init__(self,parent)
		self.ui = Ui_PyBirch()
		self.ui.setupUi(self)
		
		#Self is the main window.
		self.setWindowTitle("Py-Birch "+self._version)

		self.config = Properties()
		
	#	self.config = configparser.ConfigParser(allow_no_value=True)
	#	try:
	#		if os.path.isfile("py-birch.cfg"):
	#			self.config.read("py-birch.cfg")
	#	except:
	#		self.config.add_section("IRC_Server")
	#		self.config.set("IRC_Server", "Server", "irc.dal.net")
		
		Gui = self
		#QtCore.QObject.connect(irc_Connection,QtCore.SIGNAL("incomming"),self.update_editorWindow);
		
		self.irc_Connection = IrcConnection(self.config)
		self.server_OutputSorter = ServerOutputSorter(self.config,self.plugins)
		self.channelArray = dict()
		
		#channelWindow = Channel()

		#self.ui.mdiArea.addSubWindow(channelWindow)
		#channelWindow.show()

		layout = QGridLayout()
		
		self.statusWindow = Channel("Status", self.config,self.plugins, Channel.STATUS)
		#self.ui.Status.setLayout(layout)	
		self.ui.mdiArea.addSubWindow(self.statusWindow)
		
		#add a button to the button bar
		btn_Status = QtWidgets.QPushButton("Status")
		self.statusWindow.set_button(btn_Status)
		#btn_Status.resize(250, 250)
		button_bar_layout = self.ui.button_bar.layout()
		button_bar_layout.addWidget(btn_Status)
#		self.statusWindow.connect(btn_Status, QtCore.SIGNAL("clicked()"), self.statusWindow.button_click)
		btn_Status.clicked.connect(self.statusWindow.button_click)

		#Set Up Signals
		#self.setUpSignals()
	
		#self.ui.Status.setWindowTitle("Status")

		#self.ui.Status.show()
		#so who needs to know when a nickname is update.
		#PyQt4 Method
		#self.connect(self,QtCore.SIGNAL("NickChange"),self.nick_update)
		#self.connect(self,QtCore.SIGNAL("NickChange"),self.statusWindow.nick_update)
		#self.connect(self,QtCore.SIGNAL("NickChange"),self.irc_Connection.nick_update)

		self.NickChange.connect(self.nick_update)
		self.NickChange.connect(self.statusWindow.nick_update)
		self.NickChange.connect(self.irc_Connection.nick_update)

		#self.connect(self.statusWindow,QtCore.SIGNAL("UserInput"),self.send_to_server,2)
		self.statusWindow.UserInput.connect(self.send_to_server)

		#self.connect(self.irc_Connection,QtCore.SIGNAL("NickChange"), self.statusWindow.nick_update,2)
		self.irc_Connection.NickChange.connect(self.statusWindow.nick_update)

		#Qt::QueuedConnection = 2
		#self.connect(self.irc_Connection,QtCore.SIGNAL("incomming"),self.update_editorWindow, 2)
		self.irc_Connection.Incomming.connect(self.update_editorWindow)
		#self.connect(self.irc_Connection,QtCore.SIGNAL("Status"),self.update_statusWindow, 2)
		self.irc_Connection.Status.connect(self.update_statusWindow)
		#self.connect(self.irc_Connection,QtCore.SIGNAL("NickChange"), self.nick_update, 2)
		self.irc_Connection.NickChange.connect(self.nick_update)
		#self.connect(self.irc_Connection,QtCore.SIGNAL("ProcessEvents"),self.process_gui_events,2)
		self.irc_Connection.ProcessEvents.connect(self.process_gui_events)
		#self.connect(self.irc_Connection, QtCore.SIGNAL("StatusBar"), self.statusBar)
		self.irc_Connection.StatusBar.connect(self.statusBar)
		#self.connect(self.irc_Connection, QtCore.SIGNAL("Disconnect"),self.disconnect,2)
		self.irc_Connection.Disconnect.connect(self.disconnect)

		#self.irc_Connection.connect(self.irc_Connection, QtCore.SIGNAL("NickChange"), self.irc_Connection.nick_update)
		#irc_Connection.connect(irc_Connection, QtCore.SIGNAL("NickChange"), self.nick_update)
		self.irc_Connection.NickChange.connect(self.irc_Connection.nick_update)

		#self.connect(self.server_OutputSorter,QtCore.SIGNAL("join"),self.channel_join)
		self.server_OutputSorter.JOIN.connect(self.channel_join)

		#Part/Quit/Kick are all currently dealt with by the same method, but they are separated
		#In the Sorter for future-proofing (if neeeded) - done: Alpha 0.4.2.1
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("PART"), self.remove_nick)
		self.server_OutputSorter.PART.connect(self.remove_nick)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("QUIT"), self.remove_nick)
		self.server_OutputSorter.QUIT.connect(self.remove_nick)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("KICK"), self.remove_nick)
		self.server_OutputSorter.KICK.connect(self.remove_nick)

		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("NamesOnChannel"), self.channel_nicklist)
		self.server_OutputSorter.NamesOnChannel.connect(self.channel_nicklist)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("RemoveName"), self.remove_nick)
		self.server_OutputSorter.RemoveName.connect(self.remove_nick)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("nick_mode"), self.nick_mode_change)
		self.server_OutputSorter.Nick_Mode.connect(self.nick_mode_change)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("nicklist_update"), self.nicklist_update)
		self.server_OutputSorter.Nicklist_Update.connect(self.nicklist_update)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("ChannelTitle"),self.channel_title_update)
		self.server_OutputSorter.ChannelTitle.connect(self.channel_title_update)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("Notice"), self.statusBarNotice)
		self.server_OutputSorter.Notice.connect(self.statusBarNotice)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("StatusBar"), self.statusBar)
		self.server_OutputSorter.StatusBar.connect(self.statusBar)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("NickChange"), self.nick_update, 2)
		self.server_OutputSorter.NickChange.connect(self.nick_update)
		#self.connect(self.server_OutputSorter, QtCore.SIGNAL("NewNick"),self.new_nick)
		self.server_OutputSorter.NewNick.connect(self.new_nick)

		#QtCore.QObject.connect(self.ui.button_Connect,QtCore.SIGNAL("clicked()"),self.connectToServer)
		self.ui.button_Connect.clicked.connect(self.connectToServer)
		#QtCore.QObject.connect(self.ui.button_Send,QtCore.SIGNAL("clicked()"),self.sendToServer)
		#self.ui.button_Send.clicked.connect(self.sendToServer)
		#QtCore.QObject.connect(self.ui.button_Disconnect,QtCore.SIGNAL("clicked()"),self.button_disconnect)
		self.ui.button_Disconnect.clicked.connect(self.button_disconnect)
		
		#QtCore.QObject.connect(self.ui.button_Tile, QtCore.SIGNAL("clicked()"), self.tileHorizontally)
		self.ui.button_Tile.clicked.connect(self.tileHorizontally)
		#QtCore.QObject.connect(self.ui.button_Cascade,  QtCore.SIGNAL("clicked()"), self.cascade)
		self.ui.button_Cascade.clicked.connect(self.cascade)
		#QtCore.QObject.connect(self.ui.button_Properties, QtCore.SIGNAL("clicked()"), self.show_properties)
		self.ui.button_Properties.clicked.connect(self.show_properties)


		#QtCore.QObject.connect(self.ui.actionProperties, QtCore.SIGNAL("triggered()"), self.show_properties)
		self.ui.actionProperties.triggered.connect(self.show_properties)
		#QtCore.QObject.connect(self.ui.actionConnect, QtCore.SIGNAL("triggered()"), self.connectToServer)
		self.ui.actionConnect.triggered.connect(self.connectToServer)
		#QtCore.QObject.connect(self.ui.actionDisconnect,  QtCore.SIGNAL("triggered()"), self.button_disconnect)
		self.ui.actionDisconnect.triggered.connect(self.button_disconnect)

		#QtCore.QObject.connect(self.ui.actionTile, QtCore.SIGNAL("triggered()"), self.tileHorizontally)
		self.ui.actionTile.triggered.connect(self.tileHorizontally)
		#QtCore.QObject.connect(self.ui.actionCascade, QtCore.SIGNAL("triggered()"), self.cascade)
		self.ui.actionCascade.triggered.connect(self.cascade)
		#QtCore.QObject.connect(self.ui.actionAbout_Py_Birch, QtCore.SIGNAL("triggered()"), self.show_about)
		self.ui.actionAbout_Py_Birch.triggered.connect(self.show_about)



		self.pluginsMenu=self.ui.menubar.addMenu("Plugins")
		self.rescanAction=self.pluginsMenu.addAction("Rescan")
			
#		self.rescanMenu=QtGui.QAction("Rescan",self.pluginMenu)
#		self.rescanMenu.setObjectName("Rescan")

#		self.rescanAction.QtGui.QAction(self.plugins.discover_plugins())

		#QtCore.QObject.connect(self.rescanAction,QtCore.SIGNAL("triggered()"),self.plugins.discover_plugins)
		self.rescanAction.triggered.connect(self.plugins.discover_plugins)
		

		#self.ui.text_Input.installEventFilter(self)
	
		ts = TextString()

		ts.set_channel("#test")
		ts.set_nick(self._nick)
		
		self.config.saveConfig()
		self.ui.statusbar.showMessage("Loaded...")
	#	try:
	#		with open('py-birch.cfg', 'w') as configfile:
	#			self.config.write(configfile)
	#	except:
	#		print("Config Writing Fail")
#		self.channel_join(ts)

	def setUpSignals(self):
		self.NickChange = QtCore.pyqtSignal()

	def statusBarNotice(self, ts):
		
		message = "Notice From :"+ ts.get_nick()+" - "+ ts.get_message()
		
		self.statusBar(message)

	def statusBar(self, myMessage):
		self.ui.statusbar.showMessage("")
		self.ui.statusbar.showMessage(myMessage)


	def eventFilter(self, obj ,event):
		if event.type() == QtCore.QEvent.KeyPress and event.matches(QtGui.QKeySequence.InsertParagraphSeparator):
			self.sendToServer()
			return True

		return False

	def connectToServer(self):
		#print 'in file dialogue'
		self.statusWindow.append_channel_text("File Dialog Clicked. Touch me, I Rock!\n")
		try:
			self.irc_Connection.connectToIrc()
		#	if irc_Connection.is_alive():
		#			irc_Connection.run()
		#			else:
		#				irc_Connection.start()
			self.statusBar("Connecting...")
		except Disconnected:
			self.statusWindow.append_channel_text(self.ui.editor_Window.getText()+"Disconnected ", Disconnect)
			self.irc_Connection.stop()
			self.statusBar("Connection Failed")
			self.disconnect("Failed to Connect")
			
		


		#print "leaving file dialogue"

	def new_nick(self):
	
		myText, myOk = QtWidgets.QInputDialog.getText(self, 'Enter New Nickname','Nickname In Use. Enter New Nickname:')
		if myOk:
			print (myOk)
			#self.emit(QtCore.SIGNAL("NickChange"),myText)
			self.NickChange.emit(myText)
			#self.raw_sendToServer("NICK "+nick)
			self.send_to_server("NICK "+myText)

	#This method simply takes an *already formatted* string
	#and sends it to the server. It does not processing.
	#should be renamed raw_sendToServer
	def send_to_server(self, string_to_send):

	
		self.irc_Connection.sendToIrc(string_to_send)

	#This method is used for the *status* window. 
	#It is essentially depreicated, and will be cleaned up
	#and only send data without the addition of a channel in later
	#versions.
	def sendToServer(self):

		
		originalString = self.ui.text_Input.text()
		textToSend = originalString
		displayText = textToSend
	
		myTextToSwitch = textToSend.split(" ")

		if myTextToSwitch[0][0:1] == "/":
			if myTextToSwitch[0] == "/msg":
				remainderIndex = string.find(textToSend,myTextToSwitch[1])
				textToSend = "PRIVMSG "+myTextToSwitch[1]+textToSend[remainderIndex:]
				displayText = "**Messaging "+myTextToSwitch[1]+textToSend[remainderIndex:]
			else:
				textToSend = str(textToSend[1:])
				displayText = "---"+str(textToSend)
#remainderIndex=string.find(strServerOutput,":",2)
		else:
				textToSend = "PRIVMSG "+channelName+" :"+textToSend
				displayText = "["+channelName+"] "+originalString
		
		self.irc_Connection.sendToIrc(textToSend)
		displayText = html.escape(displayText)
		self.ui.editor_Window.insertHtml(displayText+"<br>")
		self.ui.text_Input.setText("")

	def button_disconnect(self):
		self.disconnect("Button Clicked")

	def close_channels(self):

		
		for chan in self.ui.mdiArea.subWindowList():
			print("<DEBUG>Disconnecting: Closing Channel Windows:"+chan.get_channel_name().lower())
			if chan.channelType == Channel.CHANNEL:
				chan.closeChannel()
				#self.channelArray[chan.get_channel_name().lower()] = None
				#del self.channelArray[chan.get_channel_name().lower()]
				#del chan

	#	self.channelArray = dict() 
			

	def disconnect(self,MyMessage):
		#print "in disconnect"
		self.irc_Connection.stop()
		self.close_channels()
		self.statusBar("Disconnected :"+MyMessage)

	def removeChannel(self):

		closedChannel = self.sender()

		ts = TextString()
		print("<DEBUG>removeChannel: Entered method : " + closedChannel.get_channel_name())

		#do I need some sanity check for it being OfType Channel?
		#for chan in channelArray:
			#if(chan.get_channel_name() == closedChannel.get_channel_name()):
		if(self.channelArray[closedChannel.get_channel_name().lower()] != None):
	#			print(chan.get_channel_name()+" removed")
			if closedChannel.channelType == Channel.CHANNEL:
				textToSend="PART "+self.channelArray[closedChannel.get_channel_name().lower()].get_channel_name()
				self.send_to_server(textToSend)
	
			self.ui.mdiArea.removeSubWindow(closedChannel)
			self.channelArray[closedChannel.get_channel_name().lower()] = None
			del self.channelArray[closedChannel.get_channel_name().lower()]

				
	def channel_nicklist(self, my_TextString):

		ts = my_TextString
		
		print("<DEBUG:start:channel_nicklist: ts.get_channel:"+ts.get_channel().lower()+" Channel Name:", self.channelArray[ts.get_channel().lower()].get_channel_name())
		
		try:
			self.channelArray[ts.get_channel().lower()].insert_nick(ts)
		except KeyError:
			print("<DEBUG>start.py:channel_nicklist:", KeyError)

	def nick_mode_change(self, my_TextString):
		
		self.channelArray[my_TextString.get_channel().lower()].nick_mode_change(my_TextString)
		print("<DEBIG> nick change fired :" +my_TextString.get_code())

	def remove_nick(self, my_TextString):
		
		ts = my_TextString

		ts.set_nick(ts.get_nick().strip())
		found=False

		#This ensures that a single True response will stop the nick
		#appearing in the status window, which is desired behaviour
		foundSwitch=False
		
		if ts.get_nick().lower().strip() == self._nick.lower().strip():
			print("<DEBUG>Remove Nick: I am leaving a channel!"+ts.get_channel())
			#Print a message in the status window that the user has left
			self.statusWindow.append_channel_text(ts.get_display_string()+"<DEBUG>-From start.remove_nick()" )	
		else:
			print("<DEBUG>Remove Nick (Channel):"+ts.get_channel()+" (nick)"+ts.get_nick())
			if ts.get_code() == "QUIT":
				#we now have to cycle through all channels!
				#we also have to check all channels, incase they are on
				#more than one
			
				for chan in self.channelArray:
					print("<DEBUG>Remove Nick:QUIT:Trying to remove:"+ts.get_nick()+"- From :"+chan)
					found=self.channelArray[chan].remove_nick(ts)	
					if found == True:
						self.channelArray[chan].append_channel_text(ts.get_display_string())
						foundSwitch=True
			else:
				print("<DEBUG>Remove "+ts.get_nick()+" for:"+ts.get_code()+" from (Channel):"+ts.get_channel()+" (Nick)"+ts.get_nick())
			
				found=self.channelArray[ts.get_channel().lower()].remove_nick(ts)
				if found==True:
					self.channelArray[ts.get_channel().lower()].append_channel_text(ts.get_display_string())
					foundSwitch=True

			if foundSwitch:
				print("<DEBUG>remove_nick:QUIT:Nickname found\n")
			else:
				print("<DEBUG>remove_nick:QUIT:Nickname not found\n")
				self.statusWindow.append_channel_text(ts.get_display_string())	
			

	def channel_title_update(self,my_TextString):
		ts = my_TextString
		#print ("<DEBUG>Channel_title_update:Channel"+my_TextString.get_channel())
		#print("<DEBUG>Channel_title_update:Title"+my_TextString.get_display_string())
		self.channelArray[ts.get_channel().lower()].set_channel_title(ts.get_display_string())

	def channel_join(self,my_TextString):

		ts = my_TextString

		myChannelName= ts.get_channel()
		print ("Chan Name "+ myChannelName)
		
		for char in ' :':
			myChannelName = myChannelName.replace(char,'')
			
		#Create the Channel Window, passing in the Channel Name

		exists=False

		#This unusuall series of if's is because of the unusuall case
		# where by chanName can be ==, which means that it is not None,
		# and testing them together passes through the if statement. 
		for chanName in self.channelArray:
			if (chanName is None):
				print("None Type")
			if(not chanName==""):
				#print("Chan Name "+chanName)
				if not (self.channelArray[chanName] is None):
					print("Channel Name " + self.channelArray[chanName].get_channel_name().lower())
					if self.channelArray[chanName].get_channel_name().lower() == myChannelName.lower():
						print("Match Found:"+chanName+"+"+myChannelName.lower())
						exists=True

		if exists:
			print("Channel "+myChannelName+" exists");

		if ts.get_nick() ==  self._nick and not exists: 

			#print ("<DEBUG:Channel:Join:>Creating " + myChannelName)
			#Adding @, so that ops notices get their own channel. 

			if str(myChannelName).startswith("#") or str(myChannelName).startswith("@"):
				channelWindow = Channel(str(myChannelName),self.config,self.plugins)

			else:
				channelWindow = Channel(str(myChannelName), self.config,self.plugins,2)

			#Pass the nickname into the channel. Could be a
			#Constructer variable.
			channelWindow.nick_update(self._nick)

			#Add the Channel to the MDI Area
			self.ui.mdiArea.addSubWindow(channelWindow)
			#Missing - Check to see if Channel Already joined.
			#- This may not be needed as this can only be fired on
			# JOIN recieved from the server. HOWEVER Channel Window
			# may still be open from Disconnect. (v0.1)
		
			#add the Channel to the ChannelArray.
			#channelArray.append(channelWindow)
			##########
			#All channel Keys must be lower case! (or the same case, but I've chosen lower case!)
			##########
			#print("<DEBUG:join:Checking Channel Name", channelWindow.get_channel_name())
			self.channelArray[channelWindow.get_channel_name().lower()] = channelWindow
			
			#Stuff to enable connection to continue to Status Window
			#self.ui.label_ChanName.setText(str(myChannelName))
			channelName = str(myChannelName)

			#Qt::QueuedConnection=2
			#self.connect(channelWindow,QtCore.SIGNAL("UserInput"),self.send_to_server,2)
			channelWindow.UserInput.connect(self.send_to_server)
			#self.connect(self.irc_Connection,QtCore.SIGNAL("NickChange"), channelWindow.nick_update,2)
			self.irc_Connection.NickChange.connect(channelWindow.nick_update)
			#self.connect(self,QtCore.SIGNAL("NickChange"),channelWindow.nick_update)
			self.NickChange.connect(channelWindow.nick_update)
			#self.connect(channelWindow,QtCore.SIGNAL("Channel_Closed"),self.removeChannel,2)
			channelWindow.Channel_Closed.connect(self.removeChannel)
			
			#add a button to the button bar
			
			button_bar_layout = self.ui.button_bar.layout()

			btn_Channel = QtWidgets.QPushButton(channelName)
			#btn_Channel.set
			button_bar_layout.addWidget(btn_Channel)
			
			btn_Channel.show()
			#channelWindow.connect(btn_Channel, QtCore.SIGNAL("clicked()"), channelWindow.button_click)
			btn_Channel.clicked.connect(channelWindow.button_click)

			channelWindow.set_button(btn_Channel)
			
			#Make the Channel Visible
			channelWindow.show()	
			#print("<DEBUG:start:join "+channelWindow.get_channel_name()+">")
			
		else:
			ts.set_channel(myChannelName)
			ts.set_message(ts.get_nick())
			self.channel_nicklist(ts)

	def update_statusWindow(self,  ircMessage):
		
		myQString = "!==!==! "
		myQString = myQString+str(ircMessage)
		myQString = QString(myQString)
		myQString = html.escape(myQString)
		self.statusWindow.append_channel_text(myQString+"<br>")

	def show_about(self):

		self.about = About()

		self.ui.mdiArea.addSubWindow(self.about)

		self.about.show_window()


	def update_editorWindow(self, ircMessage):
		#global server_outputSorter	
		
		ts = self.server_OutputSorter.sortOutput(ircMessage)	
		found = False
		
		#Quite messages are sorted elsewhere. 
		#We need to remove the messages here that are added to the window elsewehre. 
		#--- this list might become a long list, and we might need to find a better way of
		#recording if this should be generalically added. 

		print("<DEBUG>update_editorWindow:Code: "+" "+ts.get_nick()+" "+ts.get_code().lower()+" "+ts.get_channel())
		if ts.get_code() != 'QUIT' and ts.get_code() != 'PART' and ts.get_code() != 'KICK':
			try:
				if (self.channelArray[ts.get_channel().lower()] != None):
					#self.channelArray[ts.get_channel().lower()].append_channel_text(ts.get_display_string())
					self.channelArray[ts.get_channel().lower()].append_channel_ts(ts)
					found = True
				else:
					if self.channelArray[ts.get_code().lower()] != None:
						#self.channelArray[ts.get_code().lower()].append_channel_text(ts.get_display_string())
						self.channelArray[ts.get_code().lower()].append_channel_ts(ts)

						found = True
			except KeyError as e:
				print("<DEBUG>update_editorWindow:KeyError: "+ts.get_code().lower()+" "+ts.get_channel().lower()+" Error:"+ e.args[0])
				pass
		
		
	#NOTE Stauts window access need to be collected into a single method
	#	ircMessage+="\n"
			if (found == False):
				myQString = ""
				myQString = ts.get_display_string()
				myQString = QString(myQString)
				self.statusWindow.append_channel_text(myQString)	
		
		#This should stop the window from updating when scrolling
		#up and down through the channel!
		#if not self.ui.editor_Window.isHorizontalSliderPressed():

		#self.ui.editor_Window.moveCursor(11,False)
		
		del ts
		
	def nicklist_update(self, ts):
		myChannel = ts.get_channel()

		if myChannel.lower() in self.channelArray:
			print( myChannel + " exists. Trying to update " + ts.get_nick())
			self.channelArray[myChannel.lower()].nicklistupdate(ts)
			
		print (myChannel + "Looping through all channels just in case.")
		for chan in self.channelArray:
			self.channelArray[chan].nicklist_update(ts)

	def nick_update(self, myNick) :
		global _nick_
		
		#if myNick == self._nick_:
		#	#update all the channels with the new nickname
		#	for chan in self.channelArray:
		#		chan.nick_update(myNick)
			
		
		_nick_ = myNick
		self._nick=myNick
		self.statusWindow.nick_update(myNick)
	
	def process_gui_events(self):
		global app
		app.processEvents()	

	def tile(self):
		self.ui.mdiArea.tilesSubWindows()

#The numbers seem to be a bit backwards because it's WIDTH, then HEIGHT
	def tileHorizontally(self):

		self._layout = self.const_TILE
		#self.ui.mdiArea.tileSubWindows()
		subWindowList = self.ui.mdiArea.subWindowList()
		
		windowCount=0
		
		#So the calculation works out properly, and ignores minimised windows.
		for window in subWindowList:
			if not window.isMinimized() and not window.isHidden():
				windowCount = windowCount+1
		
		#windowHeight =  self.ui.mdiArea.height() / len(subWindowList)
		 
		windowHeight = self.ui.mdiArea.height() / windowCount
		
		#print(len(subWindowList), windowHeight,  self.ui.mdiArea.width())
		x = 0
		
		for window in subWindowList:
			if not window.isMinimized():
				window.resize(self.ui.mdiArea.width(),  windowHeight)
				window.move(0, x)
				x = x+ windowHeight
	
	def getProperties(self):
		
		return self.config()
		
	def show_properties(self):
		
		self.config.show_window()
	
	
	def cascade(self):
		self.ui.mdiArea.cascadeSubWindows()
		self._layout=self.const_CASCADE

	def closeEvent(self, event):
		
		
		try:
			self.config.saveConfig()
			self.irc_Connection.disconnect()
		except IOError as err:
			print (err)
		except OSError as err:
			print (err)
		except Exception as err:
			print("Final Error : ")
			print(err)

	def resizeEvent(self,event):

		if(self._layout==self.const_NONE):
			print("Do nothing, layout is empty")
		
		if(self._layout==self.const_TILE):
			#print("Tiling Layout")
			self.tileHorizontally()

		if(self._layout == self.const_CASCADE):
			#print("Cascde Layout")
			self.cascade()

if __name__ == "__main__":
	global app
	app = QApplication(sys.argv)
	myapp= StartQT5()
	myapp.show()
	sys.exit(app.exec_())

