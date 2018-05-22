file = open("input.txt",'r')

grid = []

for line in file:
    grid.append(line)

for i, ch in enumerate(grid[0]):
    if ch == '|':
        col = i
        break

row = 0
dir = 'D'
letters = "" 
steps = 0

while True:
    loc = grid[row][col]

    if loc.isspace():
        break

    steps += 1

    if dir == 'D':
        if loc == "+":
            if not grid[row][col+1].isspace():
                col += 1
                dir = 'R'
            elif not grid[row][col-1].isspace():
                col -= 1
                dir = 'L'
            else:
                break
        else:
            if loc.isalpha():
                letters += loc
            row += 1

    elif dir == 'U':
        if loc == "+":
            if not grid[row][col+1].isspace():
                col += 1
                dir = 'R'
            elif not grid[row][col-1].isspace():
                col -= 1
                dir = 'L'
            else:
                break
        else:
            if loc.isalpha():
                letters += loc
            row -= 1

    elif dir == 'R':
        if loc == "+":
            if not grid[row+1][col].isspace():
                row += 1
                dir = 'D'
            elif not grid[row-1][col].isspace():
                row -= 1
                dir = 'U'
            else:
                break
        else:
            if loc.isalpha():
                letters += loc
            col += 1

    elif dir == 'L':
        if loc == "+":
            if not grid[row+1][col].isspace():
                row += 1
                dir = 'D'
            elif not grid[row-1][col].isspace():
                row -= 1
                dir = 'U'
            else:
                break
        else:
            if loc.isalpha():
                letters += loc
            col -= 1

print(letters)
print(steps)