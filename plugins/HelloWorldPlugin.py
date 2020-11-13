##
#A Baisc plugin test
##
from PyBirchPlugin import PyBirchPlugin

class HelloWorldPlugin(PyBirchPlugin):

	def __init__(self):
		print("<DEBUG> Module: HelloWorld loaded")
		self._plugin_name="Hello World Plugin"
		self._plugin_version="0.1"

	def hello_world(self):
		print("Hello World")
