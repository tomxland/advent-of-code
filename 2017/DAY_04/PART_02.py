import re, sys

def getNumValid(path):

  file = open(path,'r');
  numValid = 0

  for line in file:
    array = re.split(r'\s+', line.rstrip())

    phrases = set()

    for word in array:
      phrases.add(''.join(sorted(word)))

    if len(array) == len(phrases):
      numValid += 1

  file.close()
  return numValid

print(getNumValid(sys.argv[1]))