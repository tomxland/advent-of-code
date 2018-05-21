import re

def getNumValid(path):

    file = open(path,'r');
    numValid = 0

    for line in file:
        array = re.split(r'\s+', line.rstrip())
        if len(array) == len(set(array)):
            numValid += 1

    return numValid

print(getNumValid('input.txt'))