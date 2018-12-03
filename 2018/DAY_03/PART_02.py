import re, sys

fabric = [];
size = 1000

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

def populateFabric(): 
  for i in range(0,size):
    line = [];
    for j in range(0,size):
      line.append('.');

    fabric.append(line);

def populateClaims(path):
  claims = 0;
  file = open(path,'r');

  for line in file:
    instr = re.split("[@,:x/s]+", line.strip());

    xPos = int(instr[1]);
    yPos = int(instr[2]);

    width = int(instr[3]);
    height = int(instr[4]);

    for i in range(xPos, xPos+width):
      for j in range(yPos, yPos+height):
        if fabric[i][j] == 'x':
          fabric[i][j] = '#'
        elif fabric[i][j] == '.':
          fabric[i][j] = 'x'

  return claims

def findUniqueClaim(path):
  claims = 0;
  file = open(path,'r');

  for line in file:
    instr = re.split("[@,:x/s]+", line.strip());

    isUnique = True

    xPos = int(instr[1]);
    yPos = int(instr[2]);

    width = int(instr[3]);
    height = int(instr[4]);

    for i in range(xPos, xPos+width):
      for j in range(yPos, yPos+height):
        if fabric[i][j] == '#':
          isUnique = False

    if isUnique:
      return instr[0]

  return 0

populateFabric();
populateClaims(sys.argv[1]);
print(findUniqueClaim(sys.argv[1]));