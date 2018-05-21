import re

def getMaxRegister(path):

    file = open(path,'r');
    registers = {}
    maxVal = 0

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

            if (registers[instr[0]] > maxVal):
                maxVal = registers[instr[0]]
    
    file.close()
    return maxVal

print(getMaxRegister('input.txt'))