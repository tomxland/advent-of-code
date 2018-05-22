import re, sys

def getNumSteps(path):

    file = open(path,'r');

    array = []
    steps = 0
    index = 0

    for line in file:
        array.append(int(line.strip()))

    while index <  len(array):
        offset = array[index]

        if offset >= 3:
            array[index] -= 1
        else:
            array[index] += 1

        index += offset
        steps += 1

    file.close()

    return steps

print(getNumSteps(sys.argv[1]))