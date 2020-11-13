from TextString import TextString
##
# The abstract class that is the basic plugin
##

class PyBirchPlugin:
	
	
	_pybirchmagic="PyBirchPluginMagic"

	def __init__(self):
		self._plugin_name="Py Birch Base Plugin"
		self._plugin_version="0.2"

	def hello_world(self):
		print("Abstract Class Loaded")
		return None

	def get_name(self):
		return self._plugin_name

	def get_version(self):
		return self._plugin_version

	def user_input(self,TextString):
		pass

	def server_input(self,TextString):
		pass
	##
	# Do not override this method
	##
	def get_pybirchmagic(self):
		return self._pybirchmagic
