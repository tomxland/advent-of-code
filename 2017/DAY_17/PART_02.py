import sys

afterZero = 0

offset = int(sys.argv[1])
maxTimes = 50000001

currPos = 0

for val in range(maxTimes):
  if val > 0:
    currPos = ((currPos + offset) % val) + 1
    if currPos == 1:
      afterZero = val

print(afterZero)