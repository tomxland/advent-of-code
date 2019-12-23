import sys, math
from copy import deepcopy
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
		global natPacket

		opcode = 0

		modes = [0,0,0]
		instr = self.instr[self.index]

		opcode = instr % 100
		instr //= 100

		for i in range(3):
			modes[i] = instr % 10
			instr //= 10

		if opcode == 99:
			return

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

			if self.outputCount % 3 == 0:
				self.outputNode = a
			else:
				self.packets.append(a)

			self.index += 2
			self.outputCount += 1

			#Ready to send
			if self.outputCount % 3 == 0:
				if self.outputNode == 255:
					natPacket = deepcopy(self.packets)
					self.packets = []
				else:
					for p in self.packets:
						computers[self.outputNode].setInput(p)
						
					self.packets = []
			
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
natPacket = []

lastY = None

for i in range(50):
	c = Computer(i)
	computers.append(c)

attempts = 0
found = False
while not found:
	numInputs = 0

	for c in computers:
		c.step()

	#Unpause any computers waiting on simultaneous input
	for c in computers:
		numInputs += len(c.inputs)

		if c.paused:
			c.step()

	if numInputs == 0 and len(natPacket) > 0:

		print("NAT sending %s to Computer 0" % natPacket)

		for np in natPacket:
			computers[0].setInput(np)

		if lastY == natPacket[1]:
			print("Y value %i sent from NAT twice in a row" % lastY)
			break

		lastY = natPacket[1]
		natPacket = []