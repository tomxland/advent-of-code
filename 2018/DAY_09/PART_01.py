import re, sys

NUM_PLAYERS = int(sys.argv[1])
LAST_MARBLE = int(sys.argv[2])
players = [0] * NUM_PLAYERS;

marbles = [0]
currIndex = 0;

for i in range(1, LAST_MARBLE):
  currPlayer = i % NUM_PLAYERS

  if i % 23 == 0:
    currIndex = (currIndex - 7) % len(marbles)
    removedVal = marbles.pop(currIndex)
    score = i + removedVal
    players[currPlayer] += score
  else:
    currIndex = (currIndex + 2) % len(marbles)
    marbles.insert(currIndex, i);

print("High score is", max(players))

