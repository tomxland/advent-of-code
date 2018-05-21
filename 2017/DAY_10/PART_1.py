array = []
maxSize = 256

for i in range(maxSize):
    array.append(i)

lengths = [183,0,31,146,254,240,223,150,2,206,161,1,255,232,199,88]

skipSize = 0
currPos = 0

for length in lengths:
    i = 0
    while i < length / 2:
        pos1 = (currPos + i) % maxSize
        pos2 = (currPos + length - 1 - i) % maxSize

        temp = array[pos1]
        array[pos1] = array[pos2]
        array[pos2] = temp
        i += 1

    currPos = (currPos + length + skipSize) % maxSize
    skipSize += 1

print(array[0] * array[1])