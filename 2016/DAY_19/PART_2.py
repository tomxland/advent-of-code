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

beforeSkip = start
for i in range(size//2-1):
	beforeSkip = beforeSkip.getNext()

while size > 1:
	skip = beforeSkip.getNext()
	beforeSkip.setNext(skip.getNext())
	size -= 1

	if (size % 2 == 0):
		beforeSkip = beforeSkip.getNext()

print(beforeSkip.val)

