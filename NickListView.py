#NickListView
#
#The nicklist uses a key of the nickname in LOWER CASE. 
#This is to try to ensure that case is not a problem when changing/
#deleting

from PyQt5 import  QtCore
from Nickname import Nickname
#import QtGui
#import operator
#from operator import itemgetter, attrgetter

#import sys

class NickListView(QtCore.QAbstractListModel):
	
	_version_ = "0.4"
	
	def __init__(self, parent = None):
		
		QtCore.QAbstractListModel.__init__(self, parent)
		self._nicklist = dict()
		
	def rowCount(self, parent):
		if len(self._nicklist)<=0:
			return 1
		else:
			#print("<DEBUG>NickListView.rowCount:", len(self._nicklist))
			return len(self._nicklist)
			
	
	#unused in this view
	def headerData(self, section, orientation, role):
		
		if role == QtCore.Qt.DisplayRole:
			if orientation == QtCore.Qt.Horizontal:
				return "Nick List"
				

	#This sends the data based on where it is in the list.
	def data(self, index, role):
		
		#this will eventually return the nickname.
		if role ==QtCore.Qt.ToolTipRole:
			pass
		
		#Does not work with strings. Requires Icons. TODO?
		#if role == QtCore.Qt.DecorationRole:
		#	try:
		#		itemList = list(self._nicklist.keys())
		#		row = index.row()
		#		item = self._nicklist[itemList[row]]
		#		#print (item["Status"])
		#		return item["Status"]
		#	except IndexError:
		#		return "-"
		#in python3, dictionary returns iter
		#is this efficent to use a dictionary here?
		if role == QtCore.Qt.DisplayRole:
			try:
				itemList = list(sorted(iter(self._nicklist.keys())))
				
				opList = list()
				voiceList= list()
				userList = list()
				
				for item in itemList:
					myTest = dict()
					myTest = self._nicklist[item]
					
					if ((myTest["Status"]).startswith("@")):
						opList.append(item)
					elif myTest["Status"].startswith("+"):
						voiceList.append(item)
					else:
						userList.append(item)
					
				newList =[]
				
				if opList:
					opList = sorted(opList,  key=lambda x: self._nicklist[x]["Nick"].lower())
					newList.extend(opList)
				if voiceList:
					voiceList = sorted(voiceList,  key=lambda x:self._nicklist[x]["Nick"].lower())
					newList.extend(voiceList)
				if userList:
					userList = sorted(userList, key=lambda x:self._nicklist[x]["Nick"].lower())
					newList.extend(userList)
				
				if newList:
					itemList = newList
				#itemList = list(sorted(itemList,  key=lambda x: y=self._nicklist[x]["Status"])
				#Sorts on @ and +, but it doesn't *do* anything
				#itemList = list(sorted(iter(self._nicklist.values()),  key=lambda n: n["Status"]))
				#itemList = list(sorted(iter(itemList.keys())))
				#itemList = sorted(iter(itemList))
				
				
				
				#itemList = list(sorted(iter(sorted(self._nicklist.iteritems(),  key=operator.itemgetter(1)))))
				#here we need to sort for @. I don't quite understand the sortable yet.
				row = index.row()
				item= self._nicklist[itemList[row]]
				
				return item["Status"]+item["Nick"]
			except IndexError:
				return "Empty"
		if role == QtCore.Qt.EditRole:
			try:
				itemList = list(sorted(iter(self._nicklist.keys())))
				
				opList = list()
				voiceList= list()
				userList = list()
				
				for item in itemList:
					myTest = dict()
					myTest = self._nicklist[item]
					
					if ((myTest["Status"]).startswith("@")):
						opList.append(item)
					elif myTest["Status"].startswith("+"):
						voiceList.append(item)
					else:
						userList.append(item)
					
				newList =[]
				
				if opList:
					opList = sorted(opList,  key=lambda x: self._nicklist[x]["Nick"].lower())
					newList.extend(opList)
				if voiceList:
					voiceList = sorted(voiceList,  key=lambda x:self._nicklist[x]["Nick"].lower())
					newList.extend(voiceList)
				if userList:
					userList = sorted(userList, key=lambda x:self._nicklist[x]["Nick"].lower())
					newList.extend(userList)
				
				if newList:
					itemList = newList
				#itemList = list(sorted(itemList,  key=lambda x: y=self._nicklist[x]["Status"])
				#Sorts on @ and +, but it doesn't *do* anything
				#itemList = list(sorted(iter(self._nicklist.values()),  key=lambda n: n["Status"]))
				#itemList = list(sorted(iter(itemList.keys())))
				#itemList = sorted(iter(itemList))
				
				
				
				#itemList = list(sorted(iter(sorted(self._nicklist.iteritems(),  key=operator.itemgetter(1)))))
				#here we need to sort for @. I don't quite understand the sortable yet.
				row = index.row()
				item= self._nicklist[itemList[row]]
				
				return item["Nick"]
			except IndexError:
				return "Empty"
	
				
	def insert_nick_multiple(self, myNickname):

		myNickname=myNickname.strip()

		nickname=dict()
		if myNickname.startswith("@") or myNickname.startswith("+"):
			status = myNickname[0:1]
			nickname["Status"] = status
			nickname["Nick"] = myNickname[1: ]
			#Removing any trailing spaces
			nickname["Nick"] = nickname["Nick"].strip()
		else:
			#Removing any trailing spaces
			myNickname=myNickname.strip()
			nickname["Nick"] = myNickname
			nickname["Status"] = "-"

		nickname["Host"] = ""

		myTempNickname = Nickname(nickname["Nick"])
		myTempNickname.set_status(nickname["Status"])
		myTempNickname.set_host(nickname["Host"])

		nickname["Class"]=myTempNickname
		
		#Adding in lower case as key to avoid case conflict
		self._nicklist[nickname["Nick"].lower()]=nickname
		
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		
		self.dataChanged.emit(start, finish)

	def insert_nick_single(self,  ts):

		myNickname=ts.get_message()

		myNickname=myNickname.strip()

		nickname=dict()
		if myNickname.startswith("@") or myNickname.startswith("+"):
			status = myNickname[0:1]
			nickname["Status"] = status
			nickname["Nick"] = myNickname[1: ]
			#Removing any trailing spaces
			nickname["Nick"] = nickname["Nick"].strip()
		else:
			#Removing any trailing spaces
			myNickname=myNickname.strip()
			nickname["Nick"] = myNickname
			nickname["Status"] = "-"
		
		nickname["Host"] = ts.get_nickname().get_host()
		nickname["Class"] = ts.get_nickname()

		myTempNickname = Nickname(nickname["Nick"])
		myTempNickname.set_status(nickname["Status"])
		myTempNickname.set_host(nickname["Host"])

		nickname["Class"]=myTempNickname

		#Adding in lower case as key to avoid case conflict
		self._nicklist[nickname["Nick"].lower()]=nickname
		
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		
		self.dataChanged.emit(start, finish)
	
	def remove_nick(self, myNickname):
	
		myNickname=myNickname.strip()	

		found = False
		try:
			#searching in lower case to avoid case conflict
			del self._nicklist[myNickname.lower()]
			found = True
			print("<DEBUG>NickListView:nickname found and removed: "+myNickname)
		except:
			print("<DEBUG>NickListView:nickname not found (del failed) "+myNickname)
			return False
		
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		self.dataChanged.emit(start, finish)
		
		return found
	
	def search_nick(self,  my_search_term, search_index=0):

		my_search_term=my_search_term.strip()	

			
		current_index=0
		
		for i in self._nicklist.keys():
			#print(i + my_search_term)
			if i.lower().startswith(my_search_term.lower()):
				#print ("Tab :"+i)
				if current_index == search_index:
					return self._nicklist[i]["Nick"]
				else:
					current_index=current_index+1
		else:
			return ""
			
		return""

	def search_nick_class(self,  my_search_term, search_index=0):

		my_search_term=my_search_term.strip()	

			
		current_index=0
		
		for i in self._nicklist.keys():
			#print(i + my_search_term)
			if i.lower().startswith(my_search_term.lower()):
				#print ("Tab :"+i)
				if current_index == search_index:
					try:
						if (self._nicklist[i]["Class"] != ""):
							return self._nicklist[i]["Class"]
					except KeyError:
						print("<DEBUG>NickListView:No Class Key for "+ my_search_term)
						pass	
				else:
					current_index=current_index+1
		else:
			return ""
			
		return""
	

	def insertRows(self, position, rows, parent= QtCore.QModelIndex()):
		#must be called first
		self.beginInsertRows(QtCore.QModelIndex(), position, rows+position-1)
		
		#must be called at the end.
		self.endInsertRows()
		return True
		
	def removeRows(self, position, rows, parent = QtCore.QModelIndex()):
		#must be called first
		self.beginRemoveRows(QtCore.QModelIndex(), position, rows+position-1)
		
		#must be called at the end
		self.endRemoveRows()
		return True

	def update_host(self,myNick, myNicknameClass):

		myNick = myNick.strip()
		
		if(myNick.lower() in self._nicklist.keys()):
			#print("<DEBUG>NickListView:update_host:"+ myNicknameClass.get_host())
			nickname = self._nicklist[myNick.lower()]
			nickname["Host"] = myNicknameClass.get_host()
			nickname["Class"] = myNicknameClass
			self._nicklist[myNick.lower()] = nickname
	
	#For now, just a single status is kept on everyone. There may come a point where
	#it may be desirable to keep both. This is why the check to ensure that people arn't 
	#deopped because they were voiced. 
	def changeStatus(self, myNick, myStatus):

		myNick = myNick.strip()

		if myStatus.lower() == "+v":
			nickname = self._nicklist[myNick.lower()]
			if not nickname["Status"] == "@":
				nickname["Status"] = "+"
			self._nicklist[myNick.lower()] = nickname
		elif myStatus.lower() == "+o":
			nickname = self._nicklist[myNick.lower()]
			nickname["Status"]="@"
			self._nicklist[myNick.lower()] = nickname
		elif myStatus.lower() == "-v" or myStatus.lower() == "-o":
			nickname=self._nicklist[myNick.lower()]
			nickname["Status"]=""

		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		self.dataChanged.emit(start, finish)
		
		#nickname = self._nicklist[myNick]
		#nickname["Status"] = myStatus
		#self._nicklist[myNick] = nickname
		

	############
	# This updates the nickname.
	#
	# As nicknames are held in lower case, the oldNick must be lowered
	# in order to find the right nick/status pair.
	############
	def update_nick(self, oldNick, newNick):
		
		oldNick=oldNick.strip()
		newNick=newNick.strip()

		if(oldNick.lower() in self._nicklist.keys()):
			nickname=self._nicklist[oldNick.lower()]

			newNickname=dict()
			newNickname["Nick"]=newNick
			newNickname["Status"]=nickname["Status"]
			newNickname["Host"]=nickname["Host"]

			myTempNickname = Nickname(newNickname["Nick"])
			myTempNickname.set_status(newNickname["Status"])
			myTempNickname.set_host(newNickname["Host"])

			nickname["Class"]=myTempNickname


			self.remove_nick(oldNick.lower())
			self._nicklist[newNick.lower()]=newNickname
			return True
		else:
			print("<DEBUG>:NickListView:update_nick:Old Nick not found:"+oldNick)
			return False


		#Technically the nicklist needs to be refreshed, but it
		#doesn't seem to matter.
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		self.dataChanged.emit(start, finish)
		
		#if we some-how get here, there is an error. 
		return False
