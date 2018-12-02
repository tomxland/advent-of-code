import re, sys

passwords = [];

def getPassword(path):
  file = open(path,'r');
  for line in file:
    currPassword = line.strip();

    for prevPassword in passwords:
      charDiff = 0;
      diffPos = 0;

      for i in range(0,len(prevPassword)):
        if prevPassword[i] != currPassword[i]:
          charDiff += 1;
          diffPos = i;


      if charDiff == 1:
        return currPassword[0:diffPos] + currPassword[diffPos+1:]

    passwords.append(currPassword);

  file.close()
  return "Not Found"


print(getPassword(sys.argv[1]));