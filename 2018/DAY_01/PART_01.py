import re, sys

def getFrequency(path):

  file = open(path,'r');

  sum = 0;

  for line in file:
    val = int(line);
    sum += val

  file.close()
  return sum

print(getFrequency(sys.argv[1]))