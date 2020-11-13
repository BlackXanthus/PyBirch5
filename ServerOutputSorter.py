##
# This is essentially a class that holds a single Method.
# This method, sortOutput
#
# The name is clumsy, but it works.
#
###

import sys,  html
from PyQt5 import QtCore, QtGui 
import string

#Because some Class Names are just immortal!
from TextString import TextString
from Nickname import Nickname



#Because some ClassNames are just immortal! - and I couldn't think of anything better.
class ServerOutputSorter(QtCore.QObject):

	#PyQt5 Sigals
	JOIN = QtCore.pyqtSignal(TextString)
	PART = QtCore.pyqtSignal(TextString)
	QUIT = QtCore.pyqtSignal(TextString)
	KICK = QtCore.pyqtSignal(TextString)
	NamesOnChannel = QtCore.pyqtSignal(TextString)
	RemoveName = QtCore.pyqtSignal()
	Nick_Mode = QtCore.pyqtSignal(TextString)
	Nicklist_Update = QtCore.pyqtSignal(TextString)
	ChannelTitle = QtCore.pyqtSignal(TextString)
	Notice = QtCore.pyqtSignal(TextString)
	StatusBar = QtCore.pyqtSignal()
	NickChange = QtCore.pyqtSignal()
	NewNick = QtCore.pyqtSignal()
	
	global version

	version = 0.5
	_nicknameClass = ""

	def __init__(self, my_config,my_plugins):
		self.config=my_config
		self.plugins=my_plugins
		QtCore.QObject.__init__(self)

		#This will become a more detailed section that calls in the used colours
		# and replaces non-set colours with default values. Currently it just does all or 
		# nothing
	def getTextColours(self):
		
		dict_Colour = dict()
		
		try:
			dict_Colour["Action"] = self.config.get("Text_Colours", "Action")
			dict_Colour["Mode"] = self.config.get("Text_Colours","Mode")
			dict_Colour["Join"] = self.config.get("Text_Colours","Join")
			dict_Colour["Notice"]= self.config.get("Text_Colours", "Notice")
		except:
			self.config.add_section("Text_Colours")
			self.config.set("Text_Colours","Action", "Blue")
			self.config.set("Text_Colours", "Mode","#FF0000")
			self.config.set("Text_Colours", "Join", "#00FF00")
			self.config.set("Text_Colours","Notice","#00FA55")
			
		return dict_Colour

##
# This method sorts the output from the server.
# This basically take the string from the server, and splits it
# into values for TextString. 
#
# The main aim is to ensure the TextString.code() is a valid code (PRIVMSG, MODE etc)
# and to ensure that TextString.displayString() has been formatted for visual representation.
# It should also ensure that the other values of TextString are set as much as possible, but the other
# values are not guaranteed.
#
# Takes: String
# Outputs : TextString
#
#Nick!server  Code Channel mode_settings mode_user
#:Jarus_zzzz!surrelativ@surrelativity.m1rc.net MODE #debates +v Wildblue`
	def sortOutput(self, serverOutput):
		
		
		ts = TextString()
		
		#print ("INITIAL:"+ts.get_code())
		
		dict_Colours = self.getTextColours()
		quitFound=False
		found=False
		
		splitIndex = serverOutput.find(" :",1)
		#If it doesn't find the " :" string, left side become empty, and everything
		#stops working.
		if(splitIndex <= 0):
			splitIndex=len(serverOutput)
		
		#+1 for the times when there is no :, and we end up loosing the end of the line
		leftSide = serverOutput[:splitIndex+1]
		rightSide=serverOutput[splitIndex:]
		
		#replace produces a NEW STRING!
		rightSide=rightSide.replace(":", "", 1)
		#leftSide.replace(":", "", 1)
		
		ts.set_message(rightSide)
		
		splitServerOutput = leftSide.split(" ")

		#Sort the Nick from the server
		#Yes, myFullNick is unnecessary, but i'm not recoding it now
		myFullNick = splitServerOutput[0]
		myNickIndex = splitServerOutput[0].find("!",1)
		myNick = splitServerOutput[0]

		#Replace the : with "", and python adjusts the string!
		myNick.strip()
		myNick=myNick.replace(":","",1)
		myServer=myNick
		if(myNickIndex > 0):
			myNick=myNick[0:myNickIndex-1]
			myServer=myFullNick[myNickIndex:]
			self._nicknameClass = Nickname(myNick)
			self._nicknameClass.set_host(myServer)
		else:
			self._nicknameClass = Nickname(myNick)
			myServer=myNick
			self._nicknameClass.set_host(myServer)
		
		#Set the Nick.
		ts.set_server(myServer)
		ts.set_nick(myNick)
		ts.set_display_nick(myNick)
	
		ts.set_nickname(self._nicknameClass)
		#set the Code, the powerhouse of the way this works.
		#print("Left Side:"+leftSide)
		if(len(splitServerOutput)>=2):
			ts.set_code(splitServerOutput[1])
		#print("<DEBUG>ServerOutputSorter:SortOutput(252): serverOutput "+serverOutput+"\n")
		#print("<DEBUG>ServerOutputSorter:SortOutput(252): leftSide "+leftSide+" \n")
		#print("<DEUBG>ServerOutputSorter:Sort Output(251): CODE "+ts.get_code()+" \n\n")
		
			if ts.get_code() == "NICK":
				print("[DEBUG]:ServerOutputSorter(Nick):"+rightSide)
				ts.set_mode_user(rightSide.strip())
				ts.set_display_nick(ts.get_nick())
				ts.set_display_string("<font color=\""+dict_Colours["Mode"]+"\">-===-"+ts.get_display_nick() + " has changed their nick to "+ts.get_mode_user()+"</font>")
				#self.emit(QtCore.SIGNAL("nicklist_update"),ts)
				self.Nicklist_Update.emit(ts)
				found=True
				

				
		
		#Set the Channel. The Channel here may not hold a Channel, may also hold a nickname (in the case of messages)
		#or other information.
		if(len(splitServerOutput)>=3):
			ts.set_channel(splitServerOutput[2])
			
		else:
			ts.set_channel(ts.get_server())

		#If there are more things to parse, then we have a user, and a mode setting.
		if (len(splitServerOutput) >= 4):
			ts.set_mode_settings(splitServerOutput[3])
			
			#There may be (on very, very rare occasions), more than one item in the user section
			#In order to catch them, this function finds the index of the first one, and dumps the rest
			# into TextString.mode_user()
			if(len(splitServerOutput)>=5):
			
				myIndex = leftSide.find(splitServerOutput[4])
				myUser = leftSide[myIndex:]
				ts.set_mode_user(myUser)
			
		if ts.get_code() == "JOIN":
			print("<DEBUG:ServerOutputSorter> In Join (rightSide) - "+rightSide)
			myChannel = rightSide.replace(":", "", 1)
			print("<DEBUG:ServerOutputSorter> In Join (Channel) - "+myChannel)
			ts.set_channel(myChannel)

			if (self.config.get("Nickname","HostDisplay") == "True"):
				print("<DEBUG>ServerOutputSorter:Join<font color=\""+self.config.get("Text_Colours","Join")+"\">-===-"+ts.get_display_nick()+"-"+ts.get_nickname().get_host()+" joined " +ts.get_channel()+"</font>")
				ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Join")+"\">-===-"+ts.get_display_nick()+"-"+ts.get_nickname().get_host()+" joined " +ts.get_channel()+"</font>")
			else:
				ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Join")+"\">-===-"+ts.get_display_nick()+" joined " +ts.get_channel()+"</font>")
			#ts.set_message(myMode)
			found=True
			#self.emit(QtCore.SIGNAL("join"),ts)
			self.JOIN.emit(ts)

		if ts.get_code() == "PRIVMSG":
			if not ts.get_channel().startswith("#"):
				print ("<DEBUG:ServerOutputSorter> Message "+ts.get_channel())
				tempChannel=ts.get_channel()
				ts.set_channel(ts.get_nick())
				ts.set_nick(tempChannel)
				#self.emit(QtCore.SIGNAL("join"),ts)
				self.JOIN.emit(ts)
		
			
		if ts.get_code() == "QUIT":
			ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Quit")+"\">-===-"+ts.get_display_nick()+" Quit saying: <i>" +ts.get_channel()+" "+rightSide+"</i></font>")
			#self.emit(QtCore.SIGNAL("QUIT"),ts)	
			self.QUIT.emit(ts)
			quitFound=True
			found=True
			
		if ts.get_code()=="433":

			#self.emit(QtCore.SIGNAL("NewNick"))
			self.NewNick.emit()
			found=True
			
		if ts.get_code() == "KICK":
			kick_username=splitServerOutput[3]
			ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Kick")+"\">-===-"+kick_username+" was kicked from " +ts.get_channel()+" by :"+ts.get_display_nick()+" - <i>"+rightSide+"</i></font>")
			ts.set_display_nick(ts.get_nick())
			ts.set_nick(kick_username)
			# self.emit(QtCore.SIGNAL("KICK"),ts)	
			self.KICK.emit(ts)
			found=True

		if ts.get_code() == "PART":
			ts.set_channel(splitServerOutput[2])
			ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Part")+"\">-===-"+ts.get_display_nick()+" left " +ts.get_channel()+"</font>")
			#ts.set_message(myMode)
			#self.emit(QtCore.SIGNAL("PART"),ts)
			self.PART.emit(ts)
			found=True

		if(ts.get_code() == "307"):
			ts.set_display_string("<b>("+ts.get_server()+") WHOIS "+ts.get_mode_settings()+":(Registered)</b> "+ts.get_mode_settings()+" "+rightSide)
			found=True

		if(ts.get_code() == "311"):
			ts.set_display_string("<b>("+ts.get_server()+") WHOIS "+ts.get_mode_settings()+":(User) Ident:</b>"+ts.get_mode_user()+" <b>Real Name:</b> "+rightSide)
			found=True
			
		if(ts.get_code() == "312"):
			ts.set_display_string("<b>("+ts.get_server()+") WHOIS "+ts.get_mode_settings()+":(Server)</b> "+ts.get_mode_user()+ " - "+rightSide)
			found=True
			
		if(ts.get_code() == "317"):
			ts.set_display_string("<b>("+ts.get_server()+") WHOIS "+ts.get_mode_settings()+":(Idle) :</b>"+ts.get_mode_user()+" "+rightSide)
			found=True

		if(ts.get_code() == "318"):
			#this should produce an empty line?
			found=True

		if(ts.get_code() == "319"):
			ts.set_display_string("<b>("+ts.get_server()+") WHOIS "+ts.get_mode_settings()+":(Channels)</b> "+rightSide)
			found=True



		#Now to make adjustments to the TextString.
		#there is an equals sign in position 2...
		if (ts.get_code() == "332") or (ts.get_code() == "353"):
			ts.set_channel(ts.get_channel().replace(":", "", 1))
			ts.set_channel(splitServerOutput[4])
			found=True

	

		#Why is ts. get_channel() empty at this point!?!
		if(ts.get_code()=="332"):
			ts.set_channel(splitServerOutput[3])
			ts.set_message(rightSide)
			ts.set_display_string(rightSide)
			print ("<DEBUG>ServerOutputSorter:332:Channel:"+ts.get_channel())
			print("<DEBUG>ServerOutputSorter:332:Title:"+ts.get_display_string())
			#self.emit(QtCore.SIGNAL("ChannelTitle"),ts)
			self.ChannelTitle.emit(ts)
		
		#Relies on the adjustment above!
		if ts.get_code()=="353":
			ts.set_channel(ts.get_channel().replace(":", "", 1))
			ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Join")+"\">-=== Nicknames On Channel:"+rightSide+"</font>")
			#self.emit(QtCore.SIGNAL("NamesOnChannel"), ts)
			self.NamesOnChannel.emit(ts)
			found=True
			
		if ts.get_code()=="433":

			if found != True:
				#self.emit(QtCore.SIGNAL("NewNick"))
				self.NewNick.emit()
				found=True

		#quitFound: This stops the RemoveName being run twice for QUIT. 
		#Removed Alpha 0.4.2.1 - Each section makes it's own unique call
		#if ts.get_code()=="PART" or ts.get_code()=="QUIT" or ts.get_code()=="KICK":
			#ts.set_display_string(ts.get_display_string()+"(2)")
			#if quitFound!=True:
			#	self.emit(QtCore.SIGNAL("RemoveName"), ts)
			#found=True
		
		if leftSide.startswith("PING"):
			print("<DEBUG:ServerOutputSorter> PING")
			ts.set_channel(splitServerOutput[0])
			ts.set_nick(splitServerOutput[0])
			ts.set_display_nick(splitServerOutput[0])
			ts.set_display_string("<i>"+ts.get_display_nick()+" from "+ rightSide+"</i>")
			ts.set_message(ts.get_original_string())
			found=True
		
		if ts.get_code()=="MODE" :
			myMode=""
			for i in range(3, len(splitServerOutput)):
				print("<DEBUG:ServerOutputSorter> Mode:"+splitServerOutput[i])
				if(splitServerOutput[i].strip().startswith("+")):
					ts.set_mode_settings(splitServerOutput[i])
					print ("<DEBUG:ServerOutputSorter> Mode Split:"+splitServerOutput[i])
					if (len(splitServerOutput)> (i+1)):
						ts.set_mode_user(splitServerOutput[i+1])
				if(splitServerOutput[i].strip().startswith("-")):
					ts.set_mode_settings(splitServerOutput[i])
					print ("<DEBUG:ServerOutputSorter> Mode Split:"+splitServerOutput[i])
					if(len(splitServerOutput)>(i+1)):
						ts.set_mode_user(splitServerOutput[i+1])
				
				myMode = myMode+splitServerOutput[i]+" "
			myMode.strip()

			#ts.set_mode_user(myMode)
			if not ts.get_mode_user():
				ts.set_mode_user(myMode)

			#rightSide is most often empty!
			myMode = myMode + rightSide
			#ts.set_mode_settings(rightSide)
			ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Mode")+"\">-===-"+ts.get_display_nick()+" sets mode: "+myMode+"</font>")
			ts.set_message(myMode)
			found=True

			if(ts.get_mode_settings().lower().strip()=="+r"):
				ts.set_mode_user(ts.get_channel())
				ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Mode")+"\">-===-"+ts.get_display_nick()+" sets mode :"+myMode+" on "+ts.get_mode_user()+"</font>")

			print("DEBUG:ServerOutputSorter>Mode(184) "+ts.get_mode_settings())
			if(ts.get_mode_settings().startswith("+") or ts.get_mode_settings().startswith("-")):
				if not (ts.get_mode_settings().lower().strip()=="+r"):
				#	self.emit(QtCore.SIGNAL("nick_mode"),ts)
					self.Nick_Mode.emit(ts)


				
		if ts.get_code()=="NOTICE":
			ts.set_display_nick("<font color=\""+self.config.get("Text_Colours","Notice")+"\">--Notice from "+ts.get_nick()+"--</font>")
			#self.emit(QtCore.SIGNAL("Notice"), ts)
			self.Notice.emit(ts)
			
		if ts.get_code()=="PRIVMSG":
			#now to check for action codes
			myTestString = rightSide.strip()
			#This is essentially the default place, so it doesn't matter.
			
			if myTestString.startswith("\u0001ACTION"):
				#Doesn't work!?!
				#rightSide.replace("\u0001", "")
				#myString = ts.get_display_string()
				myDisplayString = "*"+ts.get_display_nick()+" "+rightSide[9:len(rightSide)-1]
				print("<DEBUG>ServerOutputSorter:"+myDisplayString)
				ts.set_display_string("<font color=\""+self.config.get("Text_Colours","Action")+"\">"+myDisplayString+"</font>")
				found=True
		
		if (found== False):
				#print("Standard Line")
				#ts.set_channel(splitServerOutput[2])
				#splitServerIndex= serverOutput.find(ts.get_channel())
				#leftSide = serverOutput[0:splitServerIndex]
				#rightSide = origServerOutput[splitServerIndex+(len(ts.get_channel())):]
				#rightSide = rightSide.replace(":", "",1)
				
				#blank spaces are a html problem. This means I also need to sanitize the line!
				#rightSide = rightSide.replace(":", "",1)
				#rightSide=rightSide.replace(" ", "&nbsp;")
				
				rightSide = html.escape(rightSide)
				displayString="<b>("+ts.get_display_nick()+")</b> "+rightSide
				ts.set_message(rightSide)
				ts.set_display_string(displayString)
		
		#print ("Final Left Side:", leftSide, "\n Final RIGHT SIDE: ", rightSide)
		
		#ts=self.sortOutputOlder(serverOutput)

		##plugin goes here? 
		#Send the mostly formatted text string to the plugins
		self.plugins.do_server_input(ts)

		return ts
#
	def __string__(self):
		global version

		return "Server Output Sorter %d", version
