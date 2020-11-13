#This class is designed to hold information on the Nickname. 
# Mostly so that there is somewhere to hold the ISP/IP for the user
#
# This will help in being able to identify users, and making the 
# ban command something useful. 

class Nickname(object):

	_nickname = ""
	_host = ""
	_status = "-"

	def __init__(self):
		self._nickname= ""
		self._host=""
		self._status="-"

	def __init__(self, myNickname):
		self.set_nickname(myNickname)
		self._host=""
		self._status="-"


	def set_nickname(self,myNickname):
		if (myNickname.startswith("@")):
			self.set_status("@")
			myNickname = myNickname[1:myNickname]
		if (myNickname.startswith("+")):
			self.set_status("@")
			myNickname = myNickname[1:myNickname]

		self._nickname=myNickname

	def set_host(self,myHost):
		self._host=myHost

	def set_status(self, myStatus):
		self._status=myStatus

	def get_nickname(self):
		return self._nickname

	def get_host(self):
		return self._host

	def get_status(self):
		return self._status
