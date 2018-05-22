import sys, re

def getMaxRegister(path):

  file = open(path,'r');
  registers = {}

  for line in file:
    instr = re.split(r'\s+', line.rstrip())

    if (instr[0] not in registers):
      registers[instr[0]] = 0

    if (instr[4] not in registers):
      registers[instr[4]] = 0

    conditionStr = "%d %s %s" % (registers[instr[4]], instr[5], instr[6])

    if (eval(conditionStr)):
      amount = int(instr[2])

      if (instr[1] == "inc"):
        registers[instr[0]] += amount
      else:
        registers[instr[0]] -= amount
  
  file.close()
  return max(registers.values())

print(getMaxRegister(sys.argv[1]))