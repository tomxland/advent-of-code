import re, sys

elf1 = 0;
elf2 = 1;

TARGET = sys.argv[1];

recipes = [3, 7];


def printRecipes():
    for i, r in enumerate(recipes):
        if i == elf1:
            print("(%d)" % r, end='')
        elif i == elf2:
            print("[%d]" % r, end='')
        else:
            print(" %d " % r, end='')

    print('')

def getLastRecipes():
    length = len(TARGET);
    return "".join( str(x) for x in recipes[(-1*length)-1:])

lastRecipes = getLastRecipes();

while TARGET not in lastRecipes:
    nextRecipe = recipes[elf1] + recipes[elf2];

    tens = nextRecipe // 10;

    if (tens > 0):
        recipes.append(tens)

    recipes.append(nextRecipe % 10)

    #printRecipes();

    elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
    elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

    lastRecipes = getLastRecipes();

print(len(recipes) - len(TARGET))