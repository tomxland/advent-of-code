import re, sys

def getChecksum(path):
  checksum = 0;
  file = open(path,'r');

  for line in file:
    array = re.split(r'\t+', line.rstrip())

    dividend = 0
    divisor = 0
    found = False

    for index, val in enumerate(array):
      val = int(val)

      i = index + 1

      while i < len(array):
        nextVal = int(array[i])

        if (nextVal % val == 0):
          dividend = nextVal
          divisor = val
          found = True
          break
        elif (val % nextVal == 0):
          dividend = val
          divisor = nextVal
          found = True
          break

        i += 1

      if found:
        break

    checksum += dividend // divisor

  file.close()

  return checksum

print(getChecksum(sys.argv[1]))