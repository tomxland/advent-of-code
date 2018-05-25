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


particles = []

file = open(sys.argv[1],'r')
for line in file:
  args = re.split("[=<>,/s]+", line.strip())

  pos = [int(args[1]), int(args[2]), int(args[3])]
  vel = [int(args[5]), int(args[6]), int(args[7])]
  acc = [int(args[9]), int(args[10]), int(args[11])]

  particles.append(Particle(pos, vel, acc))

file.close()

for i in range(STEPS):
  for p in particles:
    p.move()

minIndex = 0
minVal = particles[0].getDistance()

for i, p in enumerate(particles):
  dist = p.getDistance() 
  if dist < minVal:
    minVal = dist
    minIndex = i
print(minIndex)

