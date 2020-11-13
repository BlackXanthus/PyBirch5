import sys, sip, string
from TextString import TextString

class UserInputSorter(): 


		def process_input(self,channel, nick,input,my_config,my_plugins):

			channelName = channel
			self._nick = nick
			self.config = my_config

			ts = TextString();
			
			ts.set_channel(channel)

			self.plugins=my_plugins


			originalString = input 
			textToSend = originalString
			displayText = textToSend

			myTextToSwitch = textToSend.split(" ")

			if myTextToSwitch[0][0:1] == "/":
				if myTextToSwitch[0].lower() == "/msg":
					#Now workds: Fixed Alpha 0.4.2.1
					lengthOfUsername = len(myTextToSwitch[1])
					remainderIndex = textToSend.find(myTextToSwitch[1])
					remainderIndex = remainderIndex+lengthOfUsername

					textToSend = "PRIVMSG "+myTextToSwitch[1]+" :"+textToSend[remainderIndex:]

					displayText = "<font color=\""+self.config.get("Text_Colours","Message")+"\">"+"***Messaging "+myTextToSwitch[1]+":"+originalString[remainderIndex:]+"</font>"

					print("<DEBUG>UIS>TextToSend:"+textToSend+" Original String:"+originalString)

				elif myTextToSwitch[0].lower() == "/notice":
					lengthOfUsername = len(myTextToSwitch[1])
					remainderIndex = textToSend.find(myTextToSwitch[1])
					remainderIndex = remainderIndex+lengthOfUsername

					textToSend = "NOTICE "+myTextToSwitch[1]+" :"+textToSend[remainderIndex:]

					displayText = "<font color=\""+self.config.get("Text_Colours","Notice")+"\">"+"***Notice "+myTextToSwitch[1]+":"+originalString[remainderIndex:]+"</font>"

					print("<DEBUG>UIS>TextToSend:"+textToSend+" Original String:"+originalString)


				elif myTextToSwitch[0].lower() == "/me":
					myText = textToSend
					textToSend = "PRIVMSG "+channelName+" :\u0001ACTION"+textToSend[3:]+"\u0001"
					displayText = "<font color=\""+self.config.get("Text_Colours","Action")+"\">"+"*"+self._nick+myText[3:]+"</font>"
				else:
					textToSend = str(textToSend[1:])
					displayText = "---"+str(textToSend)
#remainderIndex=string.find(strServerOutput,":",2)
			else:
				textToSend = "PRIVMSG "+channelName+" :"+textToSend
				displayText = "<b>["+self._nick+"]</b> "+originalString


			ts.set_display_string(displayText)
			ts.set_original_string(textToSend)
		
			self.plugins.do_user_input(ts)

			return ts
