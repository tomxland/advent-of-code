import re

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

    return numValid

print(getNumValid('input.txt'))