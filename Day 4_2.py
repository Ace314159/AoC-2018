import pathlib
import re
import operator
import collections

data = [line for line in pathlib.Path("inputs/4.txt").read_text().splitlines()]
timeR = re.compile("\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\]")
beginR = re.compile("\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] Guard #([0-9]+) begins shift")


parsed = []
for line in data:
    if line[-1] == "t":
        action = "BEGIN"
    elif line[-2] == "e":
        action = "SLEEP"
    else:
        action = "WAKE"

    if action == "BEGIN":
        p = dict(zip(("year", "month", "day", "hour", "min", "id"), map(int, beginR.search(line).groups())))
    else:
        p = dict(zip(("year", "month", "day", "hour", "min"), map(int, timeR.search(line).groups())))
    p["action"] = action
    parsed.append(p)
parsed.sort(key=operator.itemgetter("year", "month", "day", "hour", "min"))


curId = None
timesAsleep = collections.defaultdict(lambda: collections.defaultdict(int))
for action in parsed:
    if action["action"] == "BEGIN":
        curId = action["id"]
    elif action["action"] == "SLEEP":
        prevSleepMin = action["min"]
    else:
        for i in range(prevSleepMin, action["min"]):
            timesAsleep[curId][i] += 1

maxTimeAsleep = 0
maxMinute = 0
maxId = None
for id, timeAsleep in timesAsleep.items():
    for minute, time in timeAsleep.items():
        if time > maxTimeAsleep:
            maxId = id
            maxTimeAsleep = time
            maxMinute = minute

print(maxId * maxMinute)
