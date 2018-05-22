import re

def getNumSteps(path):

    file = open(path,'r');

    array = []
    steps = 0
    index = 0

    for line in file:
        array.append(int(line.strip()))

    while index <  len(array):
        offset = array[index]
        array[index] += 1
        index += offset
        steps += 1

    file.close()

    return steps

print(getNumSteps('input.txt'))