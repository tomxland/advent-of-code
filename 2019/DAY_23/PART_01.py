import sys, math
from multiprocessing import Pool

class Computer:
	def __init__(self, id):
		self.id = id
		self.instr = []
		self.index = 0
		self.base = 0
		self.outputNode = 0
		self.outputCount = 0
		self.paused = False

		self.packets = []

		file = open(sys.argv[1], 'r')
		line = file.readline().strip().split(",")
		file.close()

		for i in range(50):
			for val in line:
				self.instr.append(int(val))

			#Pad memory
			for j in range(1000):
				self.instr.append(0)

		self.inputs = [ self.id ]

	def getValue(self, i, mode):
		if mode == 0:
			return self.instr[self.instr[i]]
		elif mode == 1:
			return self.instr[i]
		else:
			pos = self.base + self.instr[i]
			return self.instr[pos]

	def getIndex(self, i, mode):
		if mode == 2:
			return self.base + self.instr[i]
		else:
			return self.instr[i]

	def setInput(self, val):
		self.inputs.append(val)

	def step(self):
		global computers
		opcode = 0

		modes = [0,0,0]
		instr = self.instr[self.index]

		opcode = instr % 100
		instr //= 100

		for i in range(3):
			modes[i] = instr % 10
			instr //= 10

		if opcode == 99:
			print("Computer %i finished" % self.id)
			return False

		elif opcode == 3:
			index = self.getIndex(self.index + 1, modes[0])
			val = -1

			if len(self.inputs) > 0:
				val = self.inputs.pop(0)
			elif not self.paused:
				self.paused = True
				return

			self.paused = False

			self.instr[index] = val
			self.index += 2

		elif opcode == 4:
			a = self.getValue(self.index+1, modes[0])

			if self.outputNode == 255:
				if self.outputCount % 3 == 2:
					print("Y value sent to 255 is %i" % a)
					return True

			elif self.outputCount % 3 == 0:
				self.outputNode = a
			else:
				self.packets.append(a)

			self.index += 2
			self.outputCount += 1

			#Ready to send
			if self.outputCount % 3 == 0:
				computers[self.outputNode].setInput(self.packets[0])
				computers[self.outputNode].setInput(self.packets[1])
				self.packets = []
				return
			
		elif opcode == 9:
			a = self.getValue(self.index+1, modes[0])
			self.base += a
			self.index += 2

		else:
			a = self.getValue(self.index+1, modes[0])
			b = self.getValue(self.index+2, modes[1])

			if opcode == 1:
				index = self.getIndex(self.index+3, modes[2])
				self.instr[index] = a + b
				self.index += 4

			elif opcode == 2:
				index = self.getIndex(self.index+3, modes[2])
				self.instr[index] = a * b
				self.index += 4

			elif opcode == 5: #jump-if-true
				if a != 0:
					self.index = b
				else:
					self.index += 3

			elif opcode == 6: #jump-if-false
				if a == 0:
					self.index = b
				else:
					self.index += 3

			elif opcode == 7: #less-than
				index = self.getIndex(self.index+3, modes[2])
				self.instr[index] = 1 if a < b else 0
				self.index += 4

			elif opcode == 8: #equals
				index = self.getIndex(self.index+3, modes[2])
				self.instr[index] = 1 if a == b else 0
				self.index += 4

computers = []

for i in range(50):
	c = Computer(i)
	computers.append(c)

found = False
while not found:
	for c in computers:
		found = c.step() or found

	#Unpause any computers waiting on simultaneous input
	for c in computers:
		if c.paused:
			found = c.step() or found

