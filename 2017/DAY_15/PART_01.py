import sys

aCurr = int(sys.argv[1])
bCurr = int(sys.argv[2])

count = 0
for i in range(40000000):
  aCurr = (aCurr * 16807) % 2147483647
  bCurr = (bCurr * 48271) % 2147483647

  mask = 0xFFFF
  aLast16 = aCurr & mask
  bLast16 = bCurr & mask

  if (aLast16 == bLast16):
    count += 1

print(count)