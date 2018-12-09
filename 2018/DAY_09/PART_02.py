import re, sys

NUM_PLAYERS = int(sys.argv[1])
LAST_MARBLE = int(sys.argv[2])
players = [0] * NUM_PLAYERS;

class Marble:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.prev = None

curr = Marble(0)
curr.next = curr
curr.prev = curr

for i in range(1, LAST_MARBLE):
  currPlayer = i % NUM_PLAYERS

  if i % 23 == 0:
    for j in range(7):
      curr = curr.prev;

    removedVal = curr.value

    currPrev = curr.prev
    curr = curr.next
    curr.prev = currPrev
    currPrev.next = curr

    score = i + removedVal
    players[currPlayer] += score

  else:
    newPrev = curr.next
    newNext = newPrev.next

    curr = Marble(i)

    newPrev.next = curr
    curr.prev = newPrev

    curr.next = newNext
    newNext.prev = curr

print("High score is", max(players))