import sys
 
def getKnotHash(input):
  array = []
  maxSize = 256

  for i in range(maxSize):
    array.append(i)


  lengths = [];
  for ch in input:
    lengths.append(ord(ch))

  lengths.extend((17, 31, 73, 47, 23))

  skipSize = 0
  currPos = 0

  for j in range(64):
    for length in lengths:
      i = 0
      while i < length / 2:
        pos1 = (currPos + i) % maxSize
        pos2 = (currPos + length - 1 - i) % maxSize

        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
        i += 1

      currPos = (currPos + length + skipSize) % maxSize
      skipSize += 1

  binStr = ''

  for i, val in enumerate(array):

    if i % 16 == 0:
      xor = 0

    xor ^= val

    if i % 16 == 15:
      binStr += bin(xor).split('b')[-1].zfill(8)

  return binStr


keyword = sys.argv[1]
count = 0
for i in range(128):
  count += getKnotHash("%s-%d" % (keyword, i)).count('1')

print(count)
