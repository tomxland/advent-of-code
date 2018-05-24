import sys

def generateNextA(prev):
  next = (prev * 16807) % 2147483647
  if (next % 4 == 0):
    return next
  else:
    return generateNextA(next)

def generateNextB(prev):
  next = (prev * 48271) % 2147483647
  if (next % 8 == 0):
    return next
  else:
    return generateNextB(next)

aCurr = int(sys.argv[1])
bCurr = int(sys.argv[2])

count = 0
for i in range(5000000):
  aCurr = generateNextA(aCurr)
  bCurr = generateNextB(bCurr)

  mask = 0xFFFF
  aLast16 = aCurr & mask
  bLast16 = bCurr & mask

  if (aLast16 == bLast16):
    count += 1

print(count)