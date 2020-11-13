
from PyQt5 import QtCore, QtGui 
#from pybirch import Ui_PyBirch
from Exceptions import Disconnected

import string
import socket
import time
import threading

class IrcConnection(QtCore.QObject,threading.Thread):

	_s = socket.socket() #create a Socket Object
	_host = socket.gethostname() # Get local machine name
	_port = 6667 # port for connection
	_destination = "irc.jara23.co.uk"
	#destination = "irc.dal.net"
	_nick = "BirchPy2"
	_realname = "Birch Python TestClient"
	_ident = "PyBirch"
	_readbuffer=""
	_stopped= False
	_config=""

	#PyQt5 Signals
	NickChange = QtCore.pyqtSignal(str)
	Incomming = QtCore.pyqtSignal(str)
	Status = QtCore.pyqtSignal(str)
	ProcessEvents = QtCore.pyqtSignal()
	StatusBar = QtCore.pyqtSignal(str)
	Disconnect = QtCore.pyqtSignal(str)

	def __init__(self, my_config):

		#Call the "super" classes *implicitly*
		threading.Thread.__init__(self)
		self._config=my_config
		#Totally counter-intuative. a Deamonic Thread is one that EXITS when the program
		#ends, rather than one that continues to run.
		self.setDaemon(True)
		QtCore.QObject.__init__(self)
		self._stopped=False

		self.setUpValues()	
		#print "initialising IRC connection"



	def setUpValues(self):
		self._port = self._config.get("IRC_Server","Port") 
		self._destination = self._config.get("IRC_Server","Server") 
		self._nick = self._config.get("IRC_Server","Nickname") 
		self._realname = self._config.get("IRC_Server","RealName")
		self._ident = self._config.get("IRC_Server","Ident") 
	
	##
	#This is going to be a little thread.
	##
	def ircServerListner(self):
		print ("Starting loop")
		#self.emit(QtCore.SIGNAL("statusBar"), "Connected to "+self._destination)
		self.StatusBar.emit("Connect to "+self._destination)

		self._readbuffer = self._s.makefile(encoding='utf8')

		#self.stopped=False
		#	for inputLine in self._readbuffer.readlines():	
	        #		print("<DEBUG:IrcConnection> inputLine>"+inputLine)
		#		self.process_input(inputLine)

		inputBuffer=""
		while not self._stopped:
			try:
				#for inputLine in self._readbuffer.readline():
				#It needs to be recv(1), as it gets a byte. There are way to many utf8 errors
				for inputLine in self._s.recv(1).decode('utf8', "ignore"):

				#	inputLine=inputLine.encode('utf8','replace')
				#	inputLine=inputLine.decode('utf8','replace')

				#	print(">"+inputLine)
					inputBuffer=inputBuffer+inputLine	

					#self.emit(QtCore.SIGNAL("processEvents"))
					if inputLine=='\n':
						#print("<DEBUG:IrcConnection> inputBuffer>"+inputBuffer)
						self.process_input(inputBuffer)	
						inputBuffer=''
				


			except UnicodeDecodeError:
				print("<DEBUG:IrcConnection: Unicode Error")

			except TimeoutError:
				print("The Socket has timed out")
				self._stopped=True
				raise Disconnected("Socket_Disconnect")
				self.Status.emit("Connection to "+self._destination+" Timed out")

			except:
				print("<IrcConnection:ircServerListner> Socket Disconnected... probably")    
				self._stopped=True
				raise Disconnected("Socket_Disconnect")


		#If we get here, it means that the buffer has been closed. 
		self._s.shutdown(socket.SHUT_RDWR)
		self._s.close()
		# self.emit(QtCore.SIGNAL("Status"),"Connection to "+self._destination+" closed")
		self.Status.emit("Connection to "+self._destination+" closed")

		
#################
#		while not self.stopped:
#			self._readbuffer=""
#			#readbuffer=readbuffer+s.recv(1024).decode('utf-8')
#			#readbuffer = readbuffer+s.recv(1024)
#			try:
#				stillWaiting = True
#				myString=""
#				#Stupid Mircosoft's codepage doesn't work well with utf8
#				#So, we need to find another way of converting to utf8
#				while stillWaiting:
#				#readbuffer = readbuffer+s.recv(1024).decode('utf8',"ignore")
#					self._readbuffer = self._s.recv(1).decode('utf8', "ignore")
#					if self._readbuffer == "\n":
#						stillWaiting = False
#					myString = myString+self._readbuffer
#			except UnicodeDecodeError:
#				print ("<DEUBG>IrcConnection:Unicode Error. Line Skipped. Bad Mojo!")
#			except:
#				print("<IrcConnection:ircServerListner> Socket Disconnected... probably")    
#				raise Disconnected("Socket_Disconnect")
#
#			#temp=string.split(readbuffer, "\n")
#			#temp=readbuffer.split("\r")
#
#
#################

	def process_input(self, inputLine):

		temp=inputLine

		#Removed to make the DEBUG output make more sense.
		#print("<DEBUG:IrcConnection>inputLine>"+temp)
		line=inputLine

		#for line in temp:
		#There is a carriage return at the end of the line.
		#This is where we strip it. 
		line=line.rstrip()
			
		#what? why am I doing this? 
		myLine=line.split(" ")

		#There is a question about wether or not these two should be here. 
		#They shold by rights be in serverOutputSorter 
		if(myLine[0]=="PING"):
			pongReply= "PONG "+myLine[1]+"\r\n"
			self._s.send(pongReply.encode('utf-8'))

		if myLine[1]=="NICK":
			myNickIndex = myLine[0].find("!", 1)
			myNickString = myLine[0]
			myNick = myNickString[1:myNickIndex]
			#splitServerOutput[0].find("!",1)
			print("<DEBUG>IrConnection:NICK:"+myNick.lower()+" "+self._nick.lower())
			if myNick.lower()==self._nick.lower():
				print("DEBUG>Changing Nick:"+myNick.lower())
				#self.emit(QtCore.SIGNAL("NickChange"), myLine[2].replace(":","",1 ))
				self.NickChange.emit(myLine[2].replace(":","",1))
						
		#self.emit(QtCore.SIGNAL("Incomming"),line)
		self.Incomming.emit(line)
		#self.emit(QtCore.SIGNAL("processEvents"))
		self.ProcessEvents.emit()
		#The sleep may not be needed with the process Events...?
		#	time.sleep(0.1)
		print ("\n<DEBUG:IrcConnection:Raw Line>"+line)

		
	def connectToIrc(self):
		ExceptionValue=113

		print ("in Connect to IRC...")
		self._stopped=False
		try:
			#Config is now "safe". Default values are provided if user
			#Has not chosen any, and errors are caught, ensuring
			#an answer is always provided.
			#self._destination = self._config.get("IRC_Server", "Server")
			#self._nick = self._config.get("IRC_Server", "Nickname")
			
			if self._destination == "":
				self._destination = self._config.get("IRC_Server","Server")
			
			#Something very bad has gone wrong if we get here!
			if self._destination =="":
				raise Disconnected("NoServerName")
				
			try:
				self._s = socket.create_connection ((self._destination,self._port),timeout=10)
				self._s.settimeout(None)
				#s = socket.socket()
				#s.connect((destination,port))
				
			except socket.error as err:
				print (err)
				raise Disconnected("Server_Disconnect")
				

			print ("in the connect...")
			#self.emit(QtCore.SIGNAL("incomming"),"connecting...")
			self.Incomming.emit("connecting...")
			#self.emit(QtCore.SIGNAL("statusBar"), "Connecting to"+self._destination)
			self.StatusBar.emit("Connecting to "+"self._destination")

			sendingNick = "NICK "+self._nick+"\r\n"
			#s.send(bytes(sendingNick,"utf-8"))
			self._s.send(sendingNick.encode('utf-8'))
			print ("Sending nick :",sendingNick)
			#self.emit(QtCore.SIGNAL("NickChange"),self._nick)
			self.NickChange.emit(self._nick)

			sendingUser = "USER "+self._nick
			sendingUser=sendingUser+" \""+self._ident+"\" \""
			sendingUser= sendingUser+self._host+"\" :"+self._realname+"\r\n"
			#s.send(bytes(sendingUser,'utf-8'));
			self._s.send(sendingUser.encode('utf-8'))
			print("Sending user:",sendingUser)

			#Move to non-blocking now that connection has been established.	
			#self._s.settimeout(0)

#		except IOError as (error, strerror):
		except IOError as strerror:
			self.emit(QtCore.SIGNAL("Status"),strerror)
			self.stopped=True
			

		self._t=threading.Thread(target=self.ircServerListner)
		self._t.start()

	def run(self):

		#set to make sure that variable isn't still set from the last disconnection
		#self._stopped=False
		try:
			self.connectToIrc()

		except Disconnected as err:
			print (err)
			myError= "Disconnected " + err.__str__()
			#self.emit(QtCore.SIGNAL("Status"), myError)
			self.Status.emit(myError)
			self.stop()

		#Because this thread will be called more than once if it gets disconnected.
		#Totally rocks my world!
		print("Ending Connection......")
		#self.emit(QtCore.SIGNAL("Status"), "Connection Closed")
		self.Status.emit("Connection Closed")
		self.disconnect()
		#threading.Thread.__init__(self)

	def stop(self):
		#self.emit(QtCore.SIGNAL("Status"), "Starting Disconnect.....")
		self.Status.emit("Starting Disconnect...")
		#self.setDaemon(False)
		self._stopped=True

		try:
			self._s.shutdown(socket.SHUT_RDWR)
			self._s.close()
		except:
			print("Socket already closed")	

		##BUG## If Diconnect (button) is clicked before connection
		####### Python will complain that no self._t exists
		if self._t is not None:
			while(self._t.is_alive()):
				print("...waiting for thread termination...")
			print("...Thread terminated")

		#self.emit(QtCore.SIGNAL("Status"),"...Disconnect complete")
		self.Status.emit("....Disconnect complete")
		
	def stopped(self):
		return True;

	def disconnect(self):
		self.stop()
		#self.emit(QtCore.SIGNAL("Disconnect"), "Disconnecting STOP")
		self.Disconnect.emit("Disconnecting STOP")

	def sendToIrc(self,myString):
		myString+="\n"

	#Requires an EXPLICIT cast to string, because it appears it arrives as a list.
	#of chars, which means only the first letter is sent.
		if(self._t.is_alive()):
			self._s.sendall(bytes((str(myString)),'utf-8'))
		else:
			#self.emit(QtCore.SIGNAL("Status"), "No Connection to "+self._destination + ". Please reconnect")
			self.Status.emit("No Connection to "+self._destination + ". Please reconnect")
			

	def nick_update(self, myNick):

		self._nick=myNick
		print ("[Debug]:IrcConnection: Updating Nick")
