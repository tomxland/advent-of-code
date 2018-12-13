import re, sys, copy

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
		for x, ch in enumerate(line):
			if (ch == 'v' or ch == '^' or ch == '<' or ch == '>'):
				letter = chr(id);
				carts[letter] = Cart(letter, ch, x, y);
				id += 1

			# Reset grid	
			if ch == 'v' or ch == '^':
				row.append('|')
			elif ch == '<' or ch == '>':
				row.append('-')
			else:
				row.append(ch)

		track.append(row);

def copyTrack():
	copy = []
	for row in track:
		copyRow = [];
		for ch in row:
			copyRow.append(ch);
		copy.append(copyRow)
	return copy;

def isSafe(ch):
	return ch == '+' or ch == "/" or ch == "|" or ch == "\\" or ch == "-"

def getLastCart():
	while len(carts) > 1:
		coords = {};

		thisTick = copyTrack();

		#have to sort carts?
		vals = list(carts.values());
		vals.sort();

		collisions = [];

		for cart in vals:
			thisTick[cart.y][cart.x] = cart.id;

		for cart in vals:
			oldX = cart.x
			oldY = cart.y

			#Find next position
			if cart.dir == '>':
				cart.x += 1
			elif cart.dir == '<':
				cart.x -= 1
			elif cart.dir == '^':
				cart.y -= 1
			elif cart.dir == 'v':
				cart.y += 1

			if isSafe(thisTick[cart.y][cart.x]):
				thisTick[cart.y][cart.x] = cart.id;
				thisTick[oldY][oldX] = track[oldY][oldX];

				nextPos = track[cart.y][cart.x];
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
			else:
				collisions.append(thisTick[cart.y][cart.x])
				collisions.append(cart.id)
				thisTick[cart.y][cart.x] = track[cart.y][cart.x]

		for letter in collisions:
			if letter in carts:
				del carts[letter];

		del thisTick;

	# Get only remaining cart 
	letter = next(iter(carts));
	cart = carts[letter];
	return (cart.x, cart.y)

getTrack(sys.argv[1])
print(getLastCart())