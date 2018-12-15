import re, sys, copy
from queue import PriorityQueue

class Player:
	def __init__(self, type, x, y):
		self.hp = 200
		self.attack = 3
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

grid = []
players = []

for y, line in enumerate(file):
	row = []
	for x, pos in enumerate(line.strip()):
		if pos == 'E' or pos == 'G':
			players.append(pos,x,y)
		row.append(pos)
	grid.append(row)

players.sort()

def findClosest(y,x,target,path):
	if grid[y][x] == target:
		return path
	elif grid[y][x] == '.':
		grid[y][x] = '?'
		moveUp = findClosest(y-1,x,target, path+'U')
		moveDown = findClosest(y+1,x,target, path+'D')
		moveLeft = findClosest(y,x-1,target, path+'L')
		moveRight = findClosest(y,x+1,target, path+'R')
	else:
		return False

def cleanGrid():
	for y in range(len(grid)):
		for x in range(len(grid[0])):
			if grid[y][x] == 'x':
				grid[y][x] = '.'

#find closest player and move towards them
for p in playerList:
	x = p.x
	y = p.y
	if p.type == 'E':
		if grid[y-1][x] = 'G':
			players[(x,y])
			#find goblin with those coords
			#decrease hp
			#if hp if < 0, kill
		elif grid[y][x-1]: 'G':
			#find goblin with those coords
			#decrease hp
			#if hp if < 0, kill
		elif grid[y][x+1]: 'G':
			#find goblin with those coords
			#decrease hp
			#if hp if < 0, kill
		elif grid[y+1][x]: 'G':
			#find goblin with those coords
			#decrease hp
			#if hp if < 0, kill
		else:
			#move to closest
