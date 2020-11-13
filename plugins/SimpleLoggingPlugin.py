###
# This is a *very simply* Login plugin
#
# It's designed to show how the system will work.
# It will be updated as new hooks and additions are added into
# the plugin system.
##
from PyBirchPlugin import PyBirchPlugin

import os.path
import time
from datetime import datetime

class SimpleLoggingPlugin(PyBirchPlugin):
	

	def __init__(self):
		self._plugin_name="Simple Loggin Plugin"
		self._plugin_version="0.2.3"
		
		self.dir="logs"	
		
		if not os.path.exists(self.dir):
			os.makedirs(self.dir)


	def user_input(self,myTextString):

		ts=myTextString

		if (ts.get_channel() == ""):
			print ("<Debug><SimpleLoggingPlugging.user_input> Empty ts.get_channel()")
		else:

			filename=self.dir+"/"+ts.get_channel().lower().strip()+"-"+self.get_file_date()+".txt"
		#	filename=self.dir+"/"+ts.get_channel().lower().strip()
		
			myInput=""
			if os.path.isfile(filename):
				myInput=open(filename,'a')
			else:
				myInput=open(filename,'w')

			myInput.write("["+self.get_date()+"]"+ts.get_display_string()+"\n")
			myInput.flush()
			myInput.close()


	def server_input(self,myTextString):

		ts=myTextString

		if(ts.get_channel() == ""):
			print ("<Debug><SimpleLoggingPluggin.server_input>Empty ts.get_channel")
		else:

			filename=self.dir+"/"+ts.get_channel().lower().strip()+"-"+self.get_file_date()+".txt"
		#	filename=self.dir+"/"+ts.get_channel().lower().strip()
		
			myInput=""
			if os.path.isfile(filename):
				myInput=open(filename,'a')
			else:
				myInput=open(filename,'w')
		
			myInput.write("["+self.get_date()+"]"+ts.get_display_string()+"\n")
			myInput.flush()
			myInput.close()

	def get_file_date(self):

		self.today=datetime.today()

		self.date=str(self.today.year)+"-"+str(self.today.month)+"-"+str(self.today.day)

		return self.date



	def get_date(self):

		self.today=datetime.today()

		self.date=str(self.today.year)+"-"+str(self.today.month)+"-"+str(self.today.day)
		self.time=str(self.today.hour)+":"+str(self.today.minute)

		now= self.date+" "+self.time

		return now

