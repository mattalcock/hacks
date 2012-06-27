
class Node():

	def __init__(self, value, next=None):
		self.value=value
		self.next = next

class LinkedList():

	def __init__(self):
		self.head=None

	def add(self, value):
		if self.head:
			last = self.head
			while(True):
				if last.next:
					last = last.next
				else:
					break
			last.next = Node(value)
		else:
			self.head = Node(value)

	def find(self, target):
		if self.head:
			r=self.head
			while(True):
				if r.value==target:
					return True
				else:
					if r.next:
						r=r.next
					else:
						return False
		else:
			return False


	def interate(self):
		if self.head:
			r=self.head
			while(True):
				print r.value
				if r.next:
					r=r.next
				else:
					break

if __name__ == '__main__':

	l = LinkedList()
	l.add(1)
	l.add(2)
	l.add(4)

	l.interate()

	print l.find(6)
	print l.find(8)
	print l.find(2)




