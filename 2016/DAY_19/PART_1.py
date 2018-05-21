elves = []
size = 3014387

class Elf:
	def __init__(self, val):
		self.val = val

	def setNext(self, next):
		self.next = next

	def getNext(self):
		return self.next

start = Elf(1)
curr = start
i = 2

while i <= size:
	next = Elf(i)
	curr.setNext(next)
	curr = next
	i += 1

curr.setNext(start)


curr = start
while size > 1:
	skip = curr.getNext()
	next = skip.getNext()
	curr.setNext(next)
	del skip
	curr = next
	size -= 1

print(curr.val)

