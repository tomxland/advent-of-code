import re, sys

def getChecksum(path):

  file = open(path,'r');

  numTwice = 0;
  numThrice = 0;

  for line in file:
  	dict = {};
  	for ch in line:
  		if ch in dict:
  			dict[ch] = dict[ch]+1;
  		else:
  			dict[ch] = 1;

  	hasTwice = False;
  	hasThrice = False;

  	for keys in dict:
  		if not hasTwice and dict[keys] == 2:
  			hasTwice = True
  			numTwice += 1;

  		if not hasThrice and dict[keys] == 3:
  			hasThrice = True
  			numThrice += 1;

  file.close()
  return numTwice * numThrice

print(getChecksum(sys.argv[1]))