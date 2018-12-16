import re, sys

register = [0,0,0,0]

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

# Correct ordering
ops = [
	gtir,
	setr,
	bori,
	gtrr,
	gtri,
	eqir,
	seti,
	eqri,
	eqrr,
	borr,
	addr,
	mulr,
	bani,
	muli,
	banr,
	addi
]

file = open(sys.argv[1], 'r')

successes = 0
count = 0

#Verify order with first part of input
while True:

	results = [];

	before = re.split("[ ,\]\[]+", file.readline().strip());
	instr = re.split("[ ,\]\[]+", file.readline().strip());
	after = re.split("[ ,\]\[]+", file.readline().strip());

	op = int(instr[0])
	a = int(instr[1])
	b = int(instr[2])
	c = int(instr[3])

	result = [int(after[1]), int(after[2]), int(after[3]), int(after[4])]

	#reset registers
	register[0] = int(before[1])
	register[1] = int(before[2])
	register[2] = int(before[3])
	register[3] = int(before[4])

	ops[op](a,b,c)

	if result[0] == register[0] and result[1] == register[1] and result[2] == register[2] and result[3] == register[3]:
		successes += 1

	count += 1

	end = file.readline().strip()

	if end == '###':
		break

print(successes)
print(count)
