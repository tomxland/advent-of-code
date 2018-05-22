import re, sys

def getNumValid(path):

  file = open(path,'r');
  numValid = 0

  for line in file:
    array = re.split(r'\s+', line.rstrip())
    if len(array) == len(set(array)):
      numValid += 1

  file.close()
  return numValid

print(getNumValid(sys.argv[1]))