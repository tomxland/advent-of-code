file = open("input.txt",'r')

lookup = {}
bridges = {}

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

def getBridges(currBridge, score, port):
    for nextPort in lookup[port]:
        component = "-%d/%d-" % (min(port,nextPort), max(port,nextPort))
        if component not in currBridge:
            nextBridge = currBridge + component
            nextScore = score + port + nextPort
            bridges[nextBridge] = nextScore
            getBridges(nextBridge, nextScore, nextPort)

getBridges("",0,0)
print(max(bridges.values()))