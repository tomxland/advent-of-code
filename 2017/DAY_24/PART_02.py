import sys

file = open(sys.argv[1],'r')

lookup = {}
lengths = {}
scores = {}

for line in file:
  string = line.strip()
  ports = string.split('/')
  port1 = int(ports[0])
  port2 = int(ports[1])

  if port1 not in lookup:
    lookup[port1] = set()

  if port2 not in lookup:
    lookup[port2] = set()

  lookup[port1].add(port2)
  lookup[port2].add(port1)

file.close()

def getBridges(currBridge, length, score, port):
  for nextPort in lookup[port]:
    component = "-%d/%d-" % (min(port,nextPort), max(port,nextPort))
    if component not in currBridge:
      nextBridge = currBridge + component
      nextScore = score + port + nextPort
      nextLength = length + 1

      lengths[nextBridge] = nextLength

      if nextLength not in scores:
        scores[nextLength] = []

      scores[nextLength].append(nextScore)
      getBridges(nextBridge, length + 1, nextScore, nextPort)

getBridges("",0,0,0)
maxLength = max(lengths.values())
print(max(scores[maxLength]))