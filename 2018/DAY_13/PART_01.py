import re, sys, copy

emptyTrack = [];
track = [];
carts = {};
turns = ['L','S','R'];


class Cart:
	def __init__(self, id, dir, x, y):
		self.id = id;
		self.dir = dir;
		self.x = x;
		self.y = y;
		self.nextTurn = 0;

	def __lt__(self,other):
		if self.y < other.y:
			return True;
		elif self.y > other.y:
			return False;
		else:
			return self.x < other.x;

	def __repr__(self):
		return "%i,%i" % (self.x, self.y)

def getTrack(path):
	id = ord('A')

	file = open(path,'r');
	# Set up carts
	for y, line in enumerate(file):
		row = []
		emptyRow = []

		for x, ch in enumerate(line):
			if (ch == 'v' or ch == '^' or ch == '<' or ch == '>'):
				letter = chr(id);
				carts[letter] = Cart(letter, ch, x, y);
				id += 1

			# Reset grid	
			if ch == 'v' or ch == '^':
				emptyRow.append('|')
				row.append(letter)
			elif ch == '<' or ch == '>':
				emptyRow.append('-')
				row.append(letter)
			else:
				emptyRow.append(ch)
				row.append(ch)

		emptyTrack.append(emptyRow);
		track.append(row);

def isSafe(ch):
	return ch == '+' or ch == "/" or ch == "|" or ch == "\\" or ch == "-"

def getIntersection():
	while len(carts) > 1:
		coords = {};

		#have to sort carts?
		vals = list(carts.values());
		vals.sort();

		collisions = [];

		for cart in vals:
			if cart.id in carts:
				nextX = cart.x
				nextY = cart.y

				#Find next position
				if cart.dir == '>':
					nextX += 1
				elif cart.dir == '<':
					nextX -= 1
				elif cart.dir == '^':
					nextY -= 1
				elif cart.dir == 'v':
					nextY += 1

				if isSafe(track[nextY][nextX]):
					track[nextY][nextX] = cart.id;
					track[cart.y][cart.x] = emptyTrack[cart.y][cart.x];

					nextPos = emptyTrack[nextY][nextX];

					if nextPos == '\\':
						if cart.dir == '>':
							cart.dir = 'v'
						elif cart.dir == '<':
							cart.dir = '^'
						elif cart.dir == '^':
							cart.dir = '<'
						elif cart.dir == 'v':
							cart.dir = '>'
					elif nextPos == '/':
						if cart.dir == '>':
							cart.dir = '^'
						elif cart.dir == '<':
							cart.dir = 'v'
						elif cart.dir == '^':
							cart.dir = '>'
						elif cart.dir == 'v':
							cart.dir = '<'
					elif nextPos == '+':
						turn = turns[cart.nextTurn]

						if (turn == 'L'):
							if cart.dir == '>':
								cart.dir = '^'
							elif cart.dir == '<':
								cart.dir = 'v'
							elif cart.dir == '^':
								cart.dir = '<'
							elif cart.dir == 'v':
								cart.dir = '>'
						elif (turn == 'R'):
							if cart.dir == '>':
								cart.dir = 'v'
							elif cart.dir == '<':
								cart.dir = '^'
							elif cart.dir == '^':
								cart.dir = '>'
							elif cart.dir == 'v':
								cart.dir = '<'

						cart.nextTurn = (cart.nextTurn + 1) % 3 

					cart.y = nextY;
					cart.x = nextX;
				else:
					return (nextX, nextY);

getTrack(sys.argv[1])
print(getIntersection())