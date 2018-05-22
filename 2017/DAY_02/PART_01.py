import re, sys

def getChecksum(path):

  file = open(path,'r');

  checksum = 0;

  for line in file:
    array = re.split(r'\t+', line.rstrip())

    min = 0;
    max = 0;

    for index, val in enumerate(array):
      val = int(val)

      if (index == 0 or val < min):
        min = val
      if (index == 0 or val > max):
        max = val

    checksum += (max - min)

  file.close()
  return checksum

print(getChecksum(sys.argv[1]))