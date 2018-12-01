import re, sys

mySet = set();

def getRepeatFrequency(path, freq):
  file = open(path,'r');
  for line in file:
    val = int(line);
    freq += val;

    if freq in mySet:
      return freq
    else:
      mySet.add(freq)

  file.close()
  return getRepeatFrequency(path, freq);


print(getRepeatFrequency(sys.argv[1], 0));