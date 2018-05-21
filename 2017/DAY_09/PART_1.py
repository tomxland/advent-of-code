def getScore(string):
    currDepth = 0
    total = 0

    for s in string:
        if s == '{':
            currDepth += 1
        elif s == '}':
            total += currDepth
            currDepth -= 1

    return total


def parseInput(string):
    while "!" in string:
        i = string.index("!")
        string = string[:i]+string[i+2:]

    while "<" in string:
        garbageStart = string.index("<")
        garbageEnd = string.index(">", garbageStart)
        string = string[:garbageStart]+string[garbageEnd+1:]

    return string

file = open("input.txt",'r');
string = file.readline().strip()

print(getScore(parseInput(string)))

