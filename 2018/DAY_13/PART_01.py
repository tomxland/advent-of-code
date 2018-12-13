import re, sys

track = [];
carts = [];
turns = ['L','S','R'];


class Cart:
	def __init__(self, id, dir, x, y):
		self.id = id;
		self.dir = dir;
		self.x = x;
		self.y = y;
		self.nextTurn = 0;


def getTrack(path):
	id = ord('A');

	file = open(path,'r');
	# Set up carts
	for y, line in enumerate(file):
		row = []
		for x, ch in enumerate(line.strip('\n')):
			if (ch == 'v' or ch == '^' or ch == '<' or ch == '>'):
				letter = chr(id)
				carts.append(Cart(letter, ch, x, y));
				id += 1

			# Reset grid	
			if ch == 'v' or ch == '^':
				row.append('|')
			elif ch == '<' or ch == '>':
				row.append('-')
			else:
				row.append(ch)

		track.append(row);


def getIntersection():
	while True:
		coords = set();
		for cart in carts:
			x = cart.x
			y = cart.y

			#Find next position
			if cart.dir == '>':
				cart.x += 1
			elif cart.dir == '<':
				cart.x -= 1
			elif cart.dir == '^':
				cart.y -= 1
			elif cart.dir == 'v':
				cart.y += 1

			str = "%i,%i" % (cart.x, cart.y);
			if str in coords:
				return (cart.x, cart.y);
			else:
				coords.add(str);

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

getTrack(sys.argv[1])
print(getIntersection())