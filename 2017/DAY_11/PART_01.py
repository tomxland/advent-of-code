import re

def getEndPoint(path)
    point = [0,0]

    file = open(path,'r');

    dirs = re.split(',',file.readline().strip())

    for d in dirs
        if d == n
            point[1] += 2
        elif d == s
            point[1] -= 2
        elif d == ne
            point[0] += 1
            point[1] += 1
        elif d == nw
            point[0] -= 1
            point[1] += 1
        elif d == se
            point[0] += 1
            point[1] -= 1
        elif d == sw
            point[0] -= 1
            point[1] -= 1

    return point

def getDistance(point)
    dist = 0

    #Move diagonally as long as you can
    while point[0] != 0 and point[1] != 0
        xStep = 1
        yStep = 1

        if (point[0]  0)
            xStep = -1
        if (point[1]  0)
            yStep = -1

        point[0] += xStep
        point[1] += yStep
        dist += 1

    if point[0] == 0 #If you're on the y axis, just step updown
        dist += abs(point[1]2)
    else
        dist += abs(point[0]) #If you're on the x axis, zig zag your way back

    return dist

print(getDistance(getEndPoint(input.txt)))