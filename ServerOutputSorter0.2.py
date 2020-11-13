##
# This is essentially a class that holds a single Method.
# This method, sortOutput

import sys
from PyQt4 import QtCore, QtGui 

import string

#Because some Class Names are just immortal!
from TextString import TextString

#Because some ClassNames are just immortal! - and I couldn't think of anything better.
class ServerOutputSorter(QtCore.QObject):
	global version

	version = 0.3

	def __init__(self, my_config):
		self.config=my_config
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
		except:
			self.config.add_section("Text_Colours")
			self.config.set("Text_Colours","Action", "Blue")
			self.config.set("Text_Colours", "Mode","#FF0000")
			self.config.set("Text_Colours", "Join", "#00FF00")
			
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
##

	def sortOutputOlder(self, serverOutput):
		
		#hack. Ensuring that ts is DEFINATELY empty. Yet, even this doesn't work!
		ts = ""
		del ts
		ts = TextString()
		rightSide=""
		leftSide=""
		
		origServerOutput = serverOutput
		
		dict_Colours = self.getTextColours()
		
		splitServerOutput = serverOutput.split(" ")
		
		ts.set_original_string(str(serverOutput))
		
		myServer = splitServerOutput[0]
		ts.set_server(myServer.replace(":","",0))
		
		myNickIndex = splitServerOutput[0].find("!",1)
		myNick = splitServerOutput[0]
		
		#Replace the : with "", and python adjusts the string!
		myNick.strip()
		myNick=myNick.replace(":", "",1)
		if(myNickIndex > 0):
			myNick=myNick[0:myNickIndex-1]
			
		ts.set_nick(myNick)
		
		ts.set_code(splitServerOutput[1])

		if(len(splitServerOutput)==2):
			print("Ping")
			ts.set_server=splitServerOutput[0]
			ts.set_channel=splitServerOutput[0]
			ts.set_nick=splitServerOutput[1]
			ts.set_display_string("++"+ts.get_nick()+" from "+ts.get_server())
			ts.set_message(ts.get_original_string())
			
		if(len(splitServerOutput)==3):
			
			if ts.get_code() == "JOIN":
				ts.set_channel(splitServerOutput[2])
				ts.set_channel(ts.get_channel().replace(":", "",1))
				ts.set_display_string("<font color=\""+dict_Colours["Join"]+"\">-===- "+ts.get_nick()+" joined " +ts.get_channel()+"</font>")
				#ts.set_message(myMode)
				self.emit(QtCore.SIGNAL("join"),ts)
				
			if ts.get_code() == "PART":
				ts.set_channel(splitServerOutput[2])
				ts.set_channel(ts.get_channel().replace(":", "",1))
				ts.set_display_string("<font color=\""+dict_Colours["Join"]+"\">-===- "+ts.get_nick()+" left " +ts.get_channel()+"</font>")
			#ts.set_message(myMode)
			#self.emit(QtCore.SIGNAL("join"),ts)	
			
		if(len(splitServerOutput)>=4):
			
			found=False
			#mySplitString= serverOutput.replace(":", "", 1)
			ts.set_channel(splitServerOutput[2])
			splitServerIndex= serverOutput.find(ts.get_channel())
			leftSide = serverOutput[0:splitServerIndex]
			leftSide = leftSide.replace(":", "", 1)
			
			rightSide = serverOutput[splitServerIndex+(len(ts.get_channel()))+1:]
			#rightSide= serverOutput[splitServerIndex+1:]
			#rightSide = rightSide.replace(":", "",1)
			rightSide = rightSide.strip()
			
			print("Left Side: "+leftSide+" -- Right  Side : "+rightSide+" -- Channel: "+ts.get_channel())
			
			#there is an equals sign in position 2...
			if (ts.get_code() == "332") or (ts.get_code() == "353"):
				found=True
				ts.set_channel(splitServerOutput[4])
		
			#Relies on the adjustment above!
			if (ts.get_code()=="353"):
				found=True
				
				#Need to re-run the split, with the new Channel. 
				if (ts.get_channel()=="="):
					ts.set_channel(splitServerOutput[4])
				
				myDisplayIndex = rightSide.find(ts.get_channel())
				ts.set_message(rightSide[myDisplayIndex+len(ts.get_channel()):])
				ts.set_message(ts.get_message().replace(":", "", 1))
				self.emit(QtCore.SIGNAL("NamesOnChannel"), ts)
				ts.set_display_string("(<b>"+ts.get_nick()+ "</b>)  Nicknames : "+ts.get_message())
			
			if(ts.get_code()=="MODE"):
				found=True
				#Set Mode stuffs
				ts.set_channel(splitServerOutput[2])
				
				myMode=""
				for i in range(3, len(splitServerOutput)):
					found=True
					myMode = myMode+splitServerOutput[i]+" "
					myMode.strip()
					ts.set_display_string("<font color=\""+dict_Colours["Mode"]+"\">-===- "+ts.get_nick()+" "+myMode+"</font>")
					ts.set_message(myMode)
				#the rest of this string goes into set_message
			
			if ts.get_code()=="PRIVMSG":
				found=True
			#now to check for action codes
				ts.set_channel(splitServerOutput[2])
				splitServerIndex= serverOutput.find(ts.get_channel())
				leftSide = serverOutput[0:splitServerIndex]
				rightSide = serverOutput[splitServerIndex+(len(ts.get_channel())):]
				rightSide = rightSide.replace(":", "",1)
				myTestString = rightSide.strip()
				ts.set_display_string("(<b>"+ts.get_nick()+"</b>)"+rightSide)
				ts.set_message(rightSide)
				
				if rightSide.startswith("\u0001ACTION"):
					#Doesn't work!?!
					rightSide.replace(char('\u0001'), "")
					myString = ts.get_display_string()
					myDisplayString = "*"+ts.get_nick()+" "+rightSide[7:len(rightSide)-1]
					print("<DEBUG>ServerOutputSorter:"+myDisplayString)
					ts.set_display_string("<font color=\""+dict_Colours["Action"]+"\">"+myDisplayString+"</font>")
			
			if ts.get_code()=="PART" or ts.get_code()=="QUIT" or ts.get_code()=="KICK":
				self.emit(QtCore.SIGNAL("RemoveName"), ts)
				found = True
			
			if (found== False):
				#print("Standard Line")
				#ts.set_channel(splitServerOutput[2])
				#splitServerIndex= serverOutput.find(ts.get_channel())
				#leftSide = serverOutput[0:splitServerIndex]
				#rightSide = origServerOutput[splitServerIndex+(len(ts.get_channel())):]
				#rightSide = rightSide.replace(":", "",1)
				
				#blank spaces are a html problem. This means I also need to sanitize the line!
				rightSide = rightSide.replace(":", "",1)
				rightSide=rightSide.replace(" ", "&nbsp;")
				
				displayString="<b>("+ts.get_nick()+")</b> "+rightSide
				ts.set_message(rightSide)
				ts.set_display_string(displayString)
		
		#print("Server String:", myServer)
		
		#ts = self.sortOutputOld(serverOutput)
		
		return ts
##
# There is a problem with this and ipv6, which prints out in hex.
# As it currently assumes that the : is just before the line to be printed, the method fails.
# As such, the method needs to be refactored.
##
	def sortOutputOld(self,serverOutput):
		
		ts = TextString()
		
		
		try:
			actionColour = self.config.get("Text_Colours", "Action")
			modeColour = self.config.get("Text_Colours","Mode")
			joinColour = self.config.get("Text_Colours","Join")
		except:
			self.config.add_section("Text_Colours")
			self.config.set("Text_Colours","Action", "Blue")
			self.config.set("Text_Colours", "Mode","#FF0000")
			self.config.set("Text_Colours", "Join", "#00FF00")
		
	#	splitServerOutput = serverOutput.split(serverOutput)
		splitServerOutput=serverOutput.replace(":", "", 1)
		splitServerIndex= splitServerOutput.find(':')

		leftSide = splitServerOutput[0:splitServerIndex]
		rightSide = splitServerOutput[splitServerIndex+1:]
		

		splitServerOutput = serverOutput.split(' ')
		strServerOutput = str(serverOutput)
		
		ts.set_original_string(str(serverOutput))

		myServer = splitServerOutput[0]
		#ts.set_server(myServer[1:])
		ts.set_server(myServer.replace(":","",0))
		
		if len(splitServerOutput) >=2:
		   ts.set_code(splitServerOutput[1])
		   
		   if len(splitServerOutput) >=3:
		      ts.set_channel(splitServerOutput[2])
		      
#		   if len(splitServerOutput) >=4:
#		      ts.set_mode(splitServerOutput[3])

		
		myNickIndex = splitServerOutput[0].find("!",1)
		myNick = splitServerOutput[0]
		
		#Replace the : with "", and python adjusts the string!
		myNick.strip()
		myNick=myNick.replace(":", "",1)
		if(myNickIndex > 0):
			myNick=myNick[0:myNickIndex-1]
			
		ts.set_nick(myNick)
		
		displayString="("+ts.get_nick()+") "+rightSide
		
		ts.set_message(rightSide)
		ts.set_display_string(displayString)

		#Don't emit signals until all the TextString Processing is done
		
		if ts.get_code() == "JOIN":
			ts.set_display_string("<font color=\""+joinColour+"\">-===-"+ts.get_nick()+" joined " +ts.get_channel()+"</font>")
			#ts.set_message(myMode)
			self.emit(QtCore.SIGNAL("join"),ts)	

		if ts.get_code() == "PART":
			ts.set_display_string("<font color=\""+joinColour+"\">-===-"+ts.get_nick()+" left " +ts.get_channel()+"</font>")
			#ts.set_message(myMode)
			#self.emit(QtCore.SIGNAL("join"),ts)	
		
		#Now to make adjustments to the TextString.

		#there is an equals sign in position 2...
		if (ts.get_code() == "332") or (ts.get_code() == "353"):
			ts.set_channel(splitServerOutput[4])
		
		#Relies on the adjustment above!
		if ts.get_code()=="353":
			self.emit(QtCore.SIGNAL("NamesOnChannel"), ts)
			
		if ts.get_code()=="PART" or ts.get_code()=="QUIT" or ts.get_code()=="KICK":
			self.emit(QtCore.SIGNAL("RemoveName"), ts)
		
		if leftSide.startswith("PING"):
			print("<DEBUG>PING")
			ts.set_channel=splitServerOutput[0]
			ts.set_nick=splitServerOutput[1]
			ts.set_display_string("("+ts.get_nick()+") from "+rightSide)
			ts.set_message(ts.get_original_string())
		
		if ts.get_code()=="MODE" :
			myMode=""
			for i in range(3, len(splitServerOutput)):
				myMode = myMode+splitServerOutput[i]+" "
			myMode.strip()
			ts.set_display_string("<font color=\""+modeColour+"\">-===-"+ts.get_nick()+" "+myMode+"</font>")
			ts.set_message(myMode)
			
		if ts.get_code()=="PRIVMSG":
			#now to check for action codes
			myTestString = rightSide.strip()
			if myTestString.startswith("\u0001ACTION"):
				#Doesn't work!?!
				#rightSide.replace("\u0001", "")
				myString = ts.get_display_string()
				myDisplayString = "*"+ts.get_nick()+rightSide[7:len(rightSide)-1]
				print("<DEBUG>ServerOutputSorter:"+myDisplayString)
				ts.set_display_string("<font color=\""+actionColour+"\">"+myDisplayString+"</font>")
			
			
		return ts


	def __string__(self):
		global version

		return "Server Output Sorter %d", version
