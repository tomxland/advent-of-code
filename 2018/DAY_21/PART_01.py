import re, sys

START = int(sys.argv[1])
register = [START,0,0,0,0,0]

class Instruction:
	def __init__(self, op, a, b, c):
		self.op = op
		self.a = a
		self.b = b
		self.c = c
				
	def run(self):
		ops[self.op](self.a, self.b, self.c)

	def __repr__(self):
		return "%s %i %i %i" % (self.op, self.a, self.b, self.c)

# addr (add register) stores into register C the result of adding register A and register B.
def addr(a, b, c):
	register[c] = register[a] + register[b]

# addi (add immediate) stores into register C the result of adding register A and value B.
def addi(a, b, c):
	register[c] = register[a] + b

# mulr (multiply register) stores into register C the result of multiplying register A and register B.
def mulr(a, b, c):
	register[c] = register[a] * register[b]

# muli (multiply immediate) stores into register C the result of multiplying register A and value B.
def muli(a, b, c):
	register[c] = register[a] * b

# banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
def banr(a, b, c):
	register[c] = register[a] & register[b]

# bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
def bani(a, b, c):
	register[c] = register[a] & b

# borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
def borr(a, b, c):
	register[c] = register[a] | register[b]

# bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
def bori(a, b, c):
	register[c] = register[a] | b

# setr (set register) copies the contents of register A into register C. (Input B is ignored.)
def setr(a, b, c):
	register[c] = register[a]

# seti (set immediate) stores value A into register C. (Input B is ignored.)
def seti(a, b, c):
	register[c] = a	

# gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
def gtir(a, b, c):
	register[c] = 1 if a > register[b] else 0

# gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
def gtri(a, b, c):
	register[c] = 1 if register[a] > b else 0
	
# gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
def gtrr(a, b, c):
	register[c] = 1 if register[a] > register[b] else 0	
	
# eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
def eqir(a, b, c):
	register[c] = 1 if a == register[b] else 0

# eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
def eqri(a, b, c):
	register[c] = 1 if register[a] == b else 0
	
# eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
def eqrr(a, b, c):
	register[c] = 1 if register[a] == register[b] else 0

ops = {
	'addr' : addr,
	'addi' : addi,
	'mulr' : mulr,
	'muli' : muli,
	'banr' : banr,
	'bani' : bani,
	'borr' : borr,
	'bori' : bori,
	'setr' : setr,
	'seti' : seti,
	'gtir' : gtir,
	'gtri' : gtri,
	'gtrr' : gtrr,
	'eqir' : eqir,
	'eqri' : eqri,
	'eqrr' : eqrr	
}

file = open('input.txt', 'r')

successes = 0
count = 0

ip = 0
instr = []

for i, line in enumerate(file):
	
	args = line.strip().split()

	if i == 0:
		ipReg = int(args[1])
	else:
		op = args[0]
		a = int(args[1])
		b = int(args[2])
		c = int(args[3])

		instr.append(Instruction(op, a, b, c))

flag = False
count = 0
visited = set()
while ip < len(instr) and ip >= 0:
	register[ipReg] = ip
	currInstr = instr[ip]
	print("ip=%i %s\t%s" % (ip, register, currInstr))


	if ip == 28:
		if register[3] not in visited:
			visited.add(register[3])
			print(register[3])
		else:
			ip = 50000

		flag = False
		input()

	if flag:
		input()

	currInstr.run()
	ip = register[ipReg] + 1
	count += 1

print("%i instructions run with register zero at %i" % (count, START))