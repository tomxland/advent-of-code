import sys

instructions = []
regs = {}
lastPlayed = 0

file = open(sys.argv[1],'r')

def getValue(val):
  if val in regs:
    return regs[val]
  else:
    return int(val)

for line in file:
  instr = line.strip().split()
  instructions.append(instr)

  try: 
    int(instr[1])
  except ValueError:
    regs[instr[1]] = 0

file.close();

i = 0
while i < len(instructions):
  instr = instructions[i]

  if instr[0] == "jgz" and getValue(instr[1]) > 0:
    i += getValue(instr[2])
    continue

  elif instr[0] == "rcv" and getValue(instr[1]) != 0:
    print(lastPlayed)
    break

  elif instr[0] == "snd":
    val = getValue(instr[1])
    lastPlayed = val

  elif instr[0] == "set":
    regs[instr[1]] = getValue(instr[2])

  elif instr[0] == "add":
    regs[instr[1]] += getValue(instr[2])

  elif instr[0] == "mul":
    regs[instr[1]] *= getValue(instr[2])

  elif instr[0] == "mod":
    regs[instr[1]] %= getValue(instr[2])

  i += 1