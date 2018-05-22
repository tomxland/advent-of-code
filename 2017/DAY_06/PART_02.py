import sys, re

def getCycles(banks):
  log = set()
  timesFound = 0

  counter = 0
  bankTarget = "" 

  while timesFound < 2:
    #Find max
    counter += 1

    maxIndex = 0
    maxValue = 0

    for index, b in enumerate(banks):
      if b > maxValue:
        maxValue = b
        maxIndex = index

    banks[maxIndex] = 0

    for i in range(maxValue):
      offset = (maxIndex + 1 + i) % len(banks)
      banks[offset] += 1

    bankStr = ','.join(str(b) for b in banks)

    if timesFound == 0:
      if bankStr in log:
        bankTarget = bankStr
        timesFound = 1
        counter = 0
      else:
        log.add(bankStr)
    elif bankTarget == bankStr:
      timesFound = 2

  return counter

def parseInput(path):
  file = open(path,'r');
  array = re.split(r'\t+', file.readline().rstrip())

  file.close();
  return list(map(int, array));

banks = parseInput(sys.argv[1]);
print(getCycles(banks))