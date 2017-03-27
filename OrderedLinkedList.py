# This is a python program for orderes linked list

class Node:

	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next

	def setData(self, newdata):
		self.data = newdata

	def setNext(self, newnext):
		self.next = newnext

class OrderedList:
	
	def __init__(self):
		self.head = None

	def isEmpty(self):
		return self.head == None

	def add(self, item):
		current = self.head
		previous = None
		stop = False
		while current != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		if previous == None:
			temp.setNext(self.head)
			self.head = temp
		else:
			temp.setNext(current)
			previous.setNext(temp)

	def search(self, item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if cuttent.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found

	def remove(self, item):
		current = self.head
		previous = None
		found = False
		while current.getNext() != None and not found:
			if current.getData() == item:
				found = True
			else:
				previous = current
				current = current.getNext()
		if previous = None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def size(self):
		current = self.head
		count = 0
		while current != None:
			count += 1
			current = current.getNext()
		return count

	def index(self, item):
		current = self.head
		counter = 0
		while current.getData != item and current != None:
			counter += 1
			current = current.getNext()

		return counter

	def pop(self):
		current = self.head
		previous = None
		stop = False
		while current.getNext() != None and not stop:
			previous = current
			current = current.getNext()
		if previous == None:
			self.head = None
		else:
			previous.setNext(None)

	def pop(self, location):
		current = self.head
		previous = None
		stop = False
		counter = 0
		while current.getNext() != None and not stop:
			if counter == location:
				stop = True
			else:
				previous = current
				current = current.getNext()
				counter += 1
		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())