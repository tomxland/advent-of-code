import re, sys
from datetime import datetime
from queue import PriorityQueue
from collections import defaultdict

unvisited = set();
blocked = set();
blockerMap = {};
blockedMap = {};

available = PriorityQueue()
workers = [];
NUM_WORKERS = 5;
OFFSET = 4;

def getSteps(path):
  file = open(path,'r');

  for line in file:
    args = line.split();

    blocker = args[1]
    blockedStep = args[7]

    unvisited.add(blockedStep);
    unvisited.add(blocker);
    blocked.add(blockedStep);

    if blockedStep not in blockedMap:
      blockedMap[blockedStep] = ''

    blockedMap[blockedStep] += blocker;

    if blocker not in blockerMap:
      blockerMap[blocker] = list()

    blockerMap[blocker].append(blockedStep);

def getTime():

  diff = unvisited.difference(blocked);
  total = 0;

  for d in diff:
    available.put(d)

  while not available.empty() or len(workers) > 0:

    i = 0;

    while i < len(workers):
      workers[i][1] -= 1

      if workers[i][1] == 0:
        visit(workers[i][0])
        workers.pop(i)
      else:
        i += 1

    while not available.empty() and len(workers) < NUM_WORKERS:
      step = available.get()
      workers.append([step, ord(step) - OFFSET])

    print(total, workers)

    total += 1

  return total - 1;

def visit(step):
  #order = "";
  unvisited.remove(step)
  #order += step;

  if step in blockerMap:
    newlyFreed = blockerMap[step];

    for freed in newlyFreed:
      blockedMap[freed] = blockedMap[freed].replace(step,"")

      if not blockedMap[freed]:
        available.put(freed)

getSteps(sys.argv[1]);
print(getTime())
