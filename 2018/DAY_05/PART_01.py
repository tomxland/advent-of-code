import sys

def react(path):
  file = open(path,'r');

  polymer = file.readline().strip();

  i = 0

  while i < len(polymer) - 1:
    if isReactive(polymer[i], polymer[i+1]):
      polymer = polymer[:i] + polymer[i+2:];
      if i != 0:
        i -= 1;
    else:
      i += 1;

  return polymer

def isReactive(a, b):
  return a.lower() == b.lower() and ((a.isupper() and b.islower()) or (a.islower() and b.isupper()))

result = react(sys.argv[1]);
print(len(result))