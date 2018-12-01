import re, sys

STEPS = 10000

class Particle:
  def __init__(self, pos, vel, acc):
    self.pos = pos
    self.vel = vel
    self.acc = acc

  def getDistance(self):
    return abs(self.pos[0]) + abs(self.pos[1]) + abs(self.pos[2])

  def move(self):
    for i in range(3):
      self.vel[i] += self.acc[i]
      self.pos[i] += self.vel[i]

  def getPosString(self):
    return "(%d,%d,%d)" % (self.pos[0], self.pos[1], self.pos[2])

particles = {}

file = open(sys.argv[1],'r')
for i, line in enumerate(file):
  args = re.split("[=<>,/s]+", line.strip())

  pos = [int(args[1]), int(args[2]), int(args[3])]
  vel = [int(args[5]), int(args[6]), int(args[7])]
  acc = [int(args[9]), int(args[10]), int(args[11])]

  particles[i] = Particle(pos, vel, acc)

file.close()

for i in range(STEPS):
  collisions = {}

  for key, p in particles.items():
    p.move()
    pos = p.getPosString()

    if pos not in collisions:
      collisions[pos] = [key]
    else:
      collisions[pos].append(key)

  for key, list in collisions.items():
    if len(list) > 1:
      for index in list:
        del particles[index]

print(len(particles))

