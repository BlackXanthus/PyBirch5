import imp,os,traceback
from PyBirchPlugin import PyBirchPlugin
from TextString import TextString
from PyQt5 import QtGui


##
# PyBirch Plugin Architecture.
#
# Built with the help of: http://eli.thegreenplace.net/2012/08/07/fundamental-concepts-of-plugin-infrastructures/
#
# see also : http://stackoverflow.com/questions/18316820/initialize-all-the-classes-in-a-module-into-nameless-objects-in-a-list
#
class PluginArchitecture:


	def __init__(self):
		self.plugins = []
		self.discover_plugins()
		self.list_plugins()

	def discover_pluginsOLD(dirs):

		for dir in dirs:
			for filename in os.listdir(dir):
				modname, ext = os.path.splittext(filename)
				if ext == '.py':
					file, path, descr = imp.find_module(modname,[dir])
					if file:
						##Loading the module register the plugin
						# in IPPluginRegistry
						mod=imp.load_module(modname,file,path,descr)
						

	def discover_plugins(self):

		self.plugins=""
		self.plugins=[]

		dir="plugins/"

		for filename in os.listdir(dir):
			modname, ext = os.path.splitext(filename)
			if ext == '.py':
				file, path, descr = imp.find_module(modname,[dir])
				if file:
					##Loading the module register the plugin
					#g in IPPluginRegistry
					print("<DEBUG:PluginArchitecture:discover_plugins> Module name: "+modname)
					#######
					# This try/except block is designed to ensure that the
					# main client doesn't stop functioning simply because
					# there's a syntax error in the loading of the module.
					#########
					try:
						mod=imp.load_module(modname,file,path,descr)
						value = getattr(mod, modname)
						if isinstance(value,type): 
							test=value()
							if test.get_pybirchmagic() == ("PyBirchPluginMagic"):
								self.plugins.append(test)
							else:
								print("Not adding "+modname+" invalid plugin")

					####
					# We still print out the stack trace so that we can troubleshoot the
					# plugin.
					####
					except:
						print("Error loading "+modname+" reason:")
						traceback.print_exc()
		self.list_plugins()

	def list_plugins(self):

		print("Listing Plugins...")	
		for plugin in self.plugins:
			try:
				print("Plugin:"+plugin.get_name()+" Version: "+plugin.get_version())
			except:
				print("Listing Plugins failed:")
				traceback.print_exc()

	def do_user_input(self,myTextString):

		ts = myTextString

		for plugin in self.plugins:
			try:
				plugin.user_input(ts)
			except:
				print("Dealing with server input for plugin name "+plugin.get_name()+" failed")
				traceback.print_exc()






	def do_server_input(self,myTextString):
		ts = myTextString

		for plugin in self.plugins:
			try:
				plugin.server_input(ts)
			except:
				print("Dealing with server input for plugin name "+plugin.get_name()+" failed")
				traceback.print_exc()



	#needs fixing! currently unused	
	def get_menu_new(self):


		rescanMenu=QtGui.QMenu("Rescan Plugins")
		rescanAction=QtGui.QAction("Rescan Plugins..",self.discover_plugins())
		rescanMenu.addAction(rescanAction)

		return rescanMenu 
	

if __name__ == "__main__":

	myclass =  PluginArchitecture()
	myclass.discover_plugins()

	print("Listing Valid Plugins:")
	myclass.list_plugins()
	print("Exiting here. Program has not crashed")


