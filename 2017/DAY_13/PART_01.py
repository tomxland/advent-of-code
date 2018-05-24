import sys
firewall = {}

def getSeverity():
  severity = 0
  for depth, range in firewall.items():
    posSize = range * 2 - 2
    pos = depth % posSize
    
    if pos > posSize/2:
      pos = posSize - pos

    if pos == 0:
      severity += (depth * range)

  return severity


def buildFirewall(path):
  file = open(path,'r');
  for line in file:
    line = line.replace(':','').strip()
    args = line.split()
    firewall[int(args[0])] = int(args[1])

buildFirewall(sys.argv[1])
print(getSeverity())