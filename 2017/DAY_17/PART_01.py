import sys

buff = []

offset = int(sys.argv[1])

maxTimes = 2018

currPos = 0

for val in range(maxTimes):
  if val > 0:
    currPos = ((currPos + offset) % val) + 1

  buff.insert(currPos,val)

nextPos = (currPos + 1) % maxTimes
print(buff[nextPos])

