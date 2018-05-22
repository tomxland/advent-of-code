import re

def getRoot(path):

    parents = set()
    children = set()

    file = open(path,'r');

    for line in file:
        args = re.split(r'[\s\->,]+',line.strip())

        if (len(args) > 2): #means it has children
            parents.add(args[0])

            i = 2
            while i < len(args):
                children.add(args[i])
                i += 1

    # find the parent that is not a child, i.e. the root
    print(parents.difference(children))

getRoot("input.txt")