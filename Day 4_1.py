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

lengthAsleep = collections.defaultdict(int)
timesAsleep = collections.defaultdict(list)

curId = None
prevSleepMin = None
for action in parsed:
    if action["action"] == "BEGIN":
        curId = action["id"]
    elif action["action"] == "SLEEP":
        prevSleepMin = action["min"]
    else:
        lengthAsleep[curId] += action["min"] - prevSleepMin
        timesAsleep[curId].append((prevSleepMin, action["min"]))

mostSleepingId = max(lengthAsleep, key=lengthAsleep.get)
timesSleeping = collections.defaultdict(int)
for time in timesAsleep[mostSleepingId]:
    for i in range(time[0], time[1]):
        timesSleeping[i] += 1
mostSleepingTime = max(timesSleeping, key=timesSleeping.get)

print(mostSleepingId * mostSleepingTime)
