
from PyQt4 import QtGui, QtCore, uic 
import operator
from operator import itemgetter, attrgetter

import sys

class NickListView(QtCore.QAbstractListModel):
	
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
				
	def insert_nick(self, myNickname):
		nickname=dict()
		if myNickname.startswith("@") or myNickname.startswith("+"):
			status = myNickname[0:1]
			nickname["Status"] = status
			nickname["Nick"] = myNickname[1: ]
		else:
			nickname["Nick"] = myNickname
			nickname["Status"] = "-"
		
		self._nicklist[nickname["Nick"]]=nickname
		
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		
		self.dataChanged.emit(start, finish)
	
	def remove_nick(self, myNickname):
		try:
			del self._nicklist[myNickname]
		except:
			print("<DEBUG>NickListView:nickname not found "+myNickname)
		
		start = self.createIndex(0, 0)
		finish = self.createIndex(len(self._nicklist), 0)
		self.dataChanged.emit(start, finish)
	
	def search_nick(self,  my_search_term):
		
		
		for i in self._nicklist.keys():
			#print(i + my_search_term)
			if i.startswith(my_search_term):
				#print ("Tab :"+i)
				return i
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
