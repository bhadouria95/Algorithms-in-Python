# This a python program that implements BST insert, preorder, postorder, and inorder traversal

class Node:
	def __init__(self, val):
		self.value = val
		self.leftChild = None
		self.rightChild = None

	def insert(self, data):
		if self.value == data:
			return False
		
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.insert(data)
			
			else:
				self.leftChild = Node(data)
				return True

		else:
			if self.rightChild:
				return self.rightChild.insert(data)
			else:
				self.rightChild = Node(data)
				return True

	def find(self, data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.leftChild:
				return self.leftChild.find(data)
			else:
				return False
		else:
			if self.rightChild:
				return self.rightChild.find(data)
			else:
				return False

	def preorder(self):
		if self:
			print(str(self.value))
			if self.leftChild:
				self.leftChild.preorder()
			if self.rightChild:
				self.rightChild.preorder()

	def postorder(self):
		if self:
			if self.leftChild:
				self.leftChild.postorder()
			if self.rightChild:
				self.rightChild.postorder()
			print(str(self.value))
			
	def inorder(self):
		if self:
			if self.leftChild:
				self.leftChild.inorder()
			print(str(self.value))
			if self.rightChild:
				self.rightChild.inorder()			

class Tree:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root  = Node(data)
			return True

	def find(self, data):
		if self.root:
			return self.root.find(data)
		else:
			return False

	def remove(self,data):
		if self.root is None:
			return False

		# Data node ir=s root node
		elif self.root.value == data:
			if self.root.leftChild is None and self.root.rightChild is None:
				self.root = None
			elif self.root.leftChild and self.root.rightChild is None:
				self.root = self.root.leftChild
			elif self.root.leftChild is None and self.root.rightChild:
				self.root = self.root.rightChild
			elif self.root.leftChild and self.root.rightChild:
				delNodeParent = self.root
				delNode = self.root.rightChild
				while delNode.leftChild:
					delNodeParent = delNode
					delNode = delNode.leftChild

				self.root.value = delNode.leftChild
				if delNode.rightChild:
					if delNode.

	def preorder(self):
		print("PreOrder")
		self.root.preorder()

	def postorder(self):
		print("PostOrder")
		self.root.postorder()

	def inorder(self):
		print("InOrder")
		self.root.inorder()

bst = Tree()
bst.insert(10)
print(bst.insert(15))
print(bst.insert(15))
bst.preorder()
bst.postorder()
bst.inorder()
bst.remove(15)
bst.inorder()
