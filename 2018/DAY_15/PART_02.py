import re, sys, copy
from queue import PriorityQueue

class Player:
	def __init__(self, type, x, y, attack):
		self.hp = 200
		self.attack = attack
		self.type = type
		self.x = x
		self.y = y

	def __lt__(self,other):
		if self.y < other.y:
			return True
		elif self.y > other.y:
			return False
		else:
			return self.x < other.x

file = open(sys.argv[1], 'r')

count = { 'E': 0, 'G': 0 }
attackMap = { 'E' : int(sys.argv[2]), 'G' : 3 }

grid = []
players = {}

for y, line in enumerate(file):
	row = []
	for x, pos in enumerate(line.strip()):
		if pos == 'E' or pos =='G':
			count[pos] += 1
			player = Player(pos, x, y, attackMap[pos]);
			players["%i,%i" % (x,y)] = player

		row.append(pos)
	grid.append(row)

def clearGrid():
	for i in range(len(grid)):
		for j in range(len(grid[0])):
			if grid[i][j] == '?':
				grid[i][j] = '.'

def movePlayer(player,target):

	#print("moving %i,%i" % (player.x,player.y))

	q = PriorityQueue();
	foundPathSize = sys.maxsize
	foundScore = sys.maxsize

	directions = set()

	q.put((0, player.y, player.x, "",""));
	grid[player.y][player.x] = '.'

	while not q.empty():
		obj = q.get()
		pathSize = obj[0]
		y = obj[1]
		x = obj[2]
		path = obj[3]
		visited = obj[4]
		
		point = "(%i,%i)" % (x,y)
		if point not in visited and pathSize <= foundPathSize:
			visited += point

			if grid[y][x] == target:
				foundPathSize = pathSize
				score = y*len(grid) + x

				if score < foundScore:
					foundScore = score
					directions.clear()
					directions.add(path[0])
				elif score == foundScore:
					directions.add(path[0])

			elif grid[y][x] == '.':
				grid[y][x] = '?'
				q.put((pathSize+1,y-1,x,path+'1',visited));
				q.put((pathSize+1,y,x-1,path+'2',visited));
				q.put((pathSize+1,y,x+1,path+'3',visited));
				q.put((pathSize+1,y+1,x,path+'4',visited));

	y = player.y
	x = player.x

	del players["%i,%i" % (x,y)]

	if '1' in directions: #up
		y -= 1
	elif '2' in directions: #left
		x -= 1
	elif '3' in directions: #right
		x += 1
	elif '4' in directions: #down
		y += 1

	grid[y][x] = player.type
	player.y = y
	player.x = x

	players["%i,%i" % (x,y)] = player
	clearGrid();

def attack(player, y, x):
	key = "%i,%i" % (x,y)

	enemy = players[key]
	enemy.hp -= player.attack

	if enemy.hp <= 0:
		#print(enemy.type, "DOWN")
		if enemy.type == 'E':
			print('Elf died')

		count[enemy.type] -= 1
		grid[enemy.y][enemy.x] = '.'
		del players[key]

#print("\n\nInitially")

#for row in grid:
#	print("".join(row));


numRounds = -1

while count['E'] > 0 and count['G'] > 0:

	playerList = list(players.values());
	playerList.sort();

	#find closest player and move towards them
	for numPlayer, iterPlayer in enumerate(playerList):
		key = "%i,%i" % (iterPlayer.x,iterPlayer.y)

		if key in players:
			p = players[key]

			if p.hp > 0:
				enemy = 'G' if p.type == 'E' else 'E'
				x = p.x
				y = p.y

				#print("player at %i,%i's turn" % (x,y))

				q = PriorityQueue()

				if grid[y-1][x] == enemy:
					key = "%i,%i" % (x,y-1)
					hp = players[key].hp 
					q.put((hp, y-1, x))
				if grid[y][x-1] == enemy:
					key = "%i,%i" % (x-1,y)
					hp = players[key].hp 
					q.put((hp, y, x-1))
				if grid[y][x+1] == enemy:
					key = "%i,%i" % (x+1,y)
					hp = players[key].hp 
					q.put((hp, y, x+1))
				if grid[y+1][x] == enemy:
					key = "%i,%i" % (x,y+1)
					hp = players[key].hp 
					q.put((hp, y+1, x))

				if not q.empty():
					attackPos = q.get()
					attack(p, attackPos[1], attackPos[2]);

					#if the last player just finished their turn
					if (count['E'] == 0 or count['G'] == 0) and numPlayer == len(playerList) - 1:
						numRounds += 1

				else:
					movePlayer(p, enemy);
					x = p.x
					y = p.y

					q = PriorityQueue()

					if grid[y-1][x] == enemy:
						key = "%i,%i" % (x,y-1)
						hp = players[key].hp 
						q.put((hp, y-1, x))
					if grid[y][x-1] == enemy:
						key = "%i,%i" % (x-1,y)
						hp = players[key].hp 
						q.put((hp, y, x-1))
					if grid[y][x+1] == enemy:
						key = "%i,%i" % (x+1,y)
						hp = players[key].hp 
						q.put((hp, y, x+1))
					if grid[y+1][x] == enemy:
						key = "%i,%i" % (x,y+1)
						hp = players[key].hp 
						q.put((hp, y+1, x))

					if not q.empty():
						attackPos = q.get()
						attack(p, attackPos[1], attackPos[2]);

						#if the last player just finished their turn
						if (count['E'] == 0 or count['G'] == 0) and numPlayer == len(playerList) - 1:
							numRounds += 1

	#print("\n\nAfter %i round(s)" % (numRounds + 1))

	#for row in grid:
	#	print("".join(row));

	numRounds += 1

	playerList = list(players.values());
	playerList.sort();

	#find closest player and move towards them
	#for numPlayer, p in enumerate(playerList):
	#	print(p.type, p.hp)

#print("Battle lasted %i rounds" % numRounds)

#print(count['E'], "left")

hpLeft = 0;

for key in players:
	hpLeft += players[key].hp

#print("Total HP left: %i" % hpLeft)

print("Battle score is %i" % (numRounds * hpLeft))

