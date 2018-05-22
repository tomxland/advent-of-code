state = 'A'

nodes = [False]
index = 0

def moveRight(index):
    index += 1
    if index >= len(nodes):
        nodes.append(False)

    return index

def moveLeft(index):
    if index == 0:
        nodes.insert(0,False)
    else:
        index -= 1

    return index

for i in range(12173597):
    if state == 'A':
        if not nodes[index]:
            nodes[index] = True
            index = moveRight(index)
            state = 'B'
        else:
            nodes[index] = False
            index = moveLeft(index)
            state = 'C'

    elif state == 'B':
        if not nodes[index]:
            nodes[index] = True
            index = moveLeft(index)
            state = 'A'
        else:
            nodes[index] = True
            index = moveRight(index)
            state = 'D'

    elif state == 'C':
        if not nodes[index]:
            nodes[index] = True
            index = moveRight(index)
            state = 'A'
        else:
            nodes[index] = False
            index = moveLeft(index)
            state = 'E'

    elif state == 'D':
        if not nodes[index]:
            nodes[index] = True
            index = moveRight(index)
            state = 'A'
        else:
            nodes[index] = False
            index = moveRight(index)
            state = 'B'

    elif state == 'E':
        if not nodes[index]:
            nodes[index] = True
            index = moveLeft(index)
            state = 'F'
        else:
            nodes[index] = True
            index = moveLeft(index)
            state = 'C'

    elif state == 'F':
        if not nodes[index]:
            nodes[index] = True
            index = moveRight(index)
            state = 'D'
        else:
            nodes[index] = True
            index = moveRight(index)
            state = 'A'

print('checksum',nodes.count(True))