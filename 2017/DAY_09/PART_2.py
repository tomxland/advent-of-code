def getGarbageTotal(string):
    garbageTotal = 0

    while "!" in string:
        i = string.index("!")
        string = string[:i]+string[i+2:]

    while "<" in string:
        garbageStart = string.index("<")
        garbageEnd = string.index(">", garbageStart)
        string = string[:garbageStart]+string[garbageEnd+1:]
        garbageTotal += (garbageEnd - garbageStart - 1)
        
    return garbageTotal

file = open("input.txt",'r');
string = file.readline().strip()

print(getGarbageTotal(string))

