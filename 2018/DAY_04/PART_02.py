import re, sys
from datetime import datetime

logs = [];
asleep = {};
minuteLog = {};

def getSchedule(path):
  file = open(path,'r');

  for line in file:
    #record = line.split();
    record = re.split("[\[\] ]+", line.strip());

    #1518-04-29 23:57
    timestamp = datetime.strptime(record[1] + " " + record[2], "%Y-%m-%d %H:%M");
    tup = (timestamp, record[3], record[4])
    logs.append(tup)

  logs.sort(key=lambda tup: tup[0])

def logSleep():
  guard = None;
  start = 0;

  for log in logs:
    if log[1] == "Guard":
      guard = log[2]
      totalAsleep = 0;

    elif log[1] == "falls":
      start = log[0].minute
    elif log[1] == "wakes":
      end = log[0].minute;

      if guard not in minuteLog:
        minuteLog[guard] = [0] * 60;

      for i in range(start, end):
        minuteLog[guard][i] += 1;

def getOptimalTime():
  maxGuard = None;
  maxAsleep = 0;
  maxMinute = 0;

  for guard in minuteLog:
    numAsleep = max(minuteLog[guard]);
    minute = minuteLog[guard].index(numAsleep);

    if numAsleep > maxAsleep:
      maxMinute = minute;
      maxGuard = guard
      maxAsleep = numAsleep;

  return (int(maxGuard.lstrip("#")), maxMinute);

getSchedule(sys.argv[1]);
logSleep();
guardTime = getOptimalTime();

print(guardTime[0]*guardTime[1])
