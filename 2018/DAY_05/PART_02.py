import sys

def getPolymer(path): 
  file = open(path,'r');

  return file.readline().strip();

def react(polymer):
  i = 0

  while i < len(polymer) - 1:
    if isReactive(polymer[i], polymer[i+1]):
      polymer = polymer[:i] + polymer[i+2:];
      if i != 0:
        i -= 1;
    else:
      i += 1;

  return polymer

def findImprovedReaction(polymer):
  minLength = len(polymer);

  letters = ''.join(set(polymer.lower()));

  for letter in letters:
    start = polymer.replace(letter,"");
    start = start.replace(letter.upper(),"");

    currLength = len(react(start));

    if currLength < minLength:
      minLength = currLength;

  return minLength;

def isReactive(a, b):
  return a.lower() == b.lower() and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))

start = getPolymer(sys.argv[1]);
print(findImprovedReaction(start));