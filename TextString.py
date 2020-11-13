#Text String. The Return
#
# After Much agonising, it seems that I really do need this class.
#
# Essentially, this class, after a string has been sorted,
# holds the original string, as well as the individual parts
# of the string in different sections for ease of access,
# and readability. 
#
#

import sys
import string

#If your wondering why it's called TextString
#Well, FU that's why!
class TextString(object):

	global _channel_, _server_, _code_, _nick_
	global _message_, _original_string_, _display_string_
	global _mode_settings_, _mode_user_, _display_nick_


	_channel_ = ""
	_server_ = ""
	_code_ = ""
	_nick_ = ""
	_display_nick_=""
	_message_ = ""
	_original_string_ = ""
	_display_string_ = ""
	_mode_settings_ = ""
	_mode_user_ = ""
	_nickname_ = ""

#we can just use the default constructor.
	def __init__(self):
		self._channel_ = ""
		self._server_ = ""
		self._code_ = ""
		self._nick_ = ""
		self._message_ = ""
		self._original_string_ = ""
		self._display_string_ = ""
		self._mode_settings_=""
		self._mode_user_ = ""
		self._display_nick_=""
		self._nickname_=""

	def set_channel(self, myChannel):
		global _channel_

		self._channel_=myChannel

	def get_channel(self):

		global _channel_
	
		return self._channel_

	def set_server(self, myServer):

		global _server_

		self._server_ = myServer

	def get_server(self):

		global _server_
		return self._server_


	def set_code(self, myCode):
		global _code_

		self._code_ = myCode


	def get_code(self):

		global _code_
		return self._code_


	def set_nick(self, myNick):

		global _nick_
		self._nick_ = myNick


	def get_nick(self):

		global _nick_

		return self._nick_

   #This nick is, for most actions, the same
   #as the standard nick, except for messages. 
	def set_display_nick(self,myNick):

		global _display_nick_
		self._display_nick_=myNick

	def get_display_nick(self):

		global _display_nick_
		return self._display_nick_


	def set_message(self, myMessage):

		global _message_

		self._message_ = myMessage


	def get_message(self):

		global _message_

		return self._message_


	def set_original_string(self, myOriginalString):

		global _original_string_

		self._original_string_ = myOriginalString


	def get_original_string(self):

		global _original_string_

		return self._original_string_


	def set_display_string(self, myDisplayString):
	
		global _display_string_

		self._display_string_ = myDisplayString


	def get_display_string(self):

		global _display_string_

		return self._display_string_
		
	def set_mode_settings(self, myModeSettings):
		
		self._mode_settings_ = myModeSettings
		
	def get_mode_settings(self):
		
		return self._mode_settings_
		
	def set_mode_user(self, myModeUser):
		
		self._mode_user_=myModeUser
		
	def get_mode_user(self):
		
		return self._mode_user_

	def set_nickname(self, myNickname):
		self._nickname_=myNickname

	def get_nickname(self):
		return self._nickname_

	def get_nickname_class(self):
		return self._nickname_
