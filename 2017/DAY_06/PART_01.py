import re, sys

def getCycles(banks):
  log = set()
  found = False

  counter = 0

  while not found:
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

    if bankStr in log:
      found = True
    else:
      log.add(bankStr)

  return counter

def parseInput(path):
  file = open(path,'r');
  array = re.split(r'\t+', file.readline().rstrip())

  file.close();
  return list(map(int, array));

banks = parseInput(sys.argv[1]);
print(getCycles(banks))