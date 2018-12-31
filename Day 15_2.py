import pathlib
from dataclasses import dataclass
import operator
import collections
import copy


@dataclass(frozen=True, eq=True)
class Pos:
    x: int
    y: int

    def isValid(self):
        return self.y < len(Map) and x < len(Map[0]) and Map[self.y][self.x] != "#"

    def getAround(self):
        temp = [Pos(self.x, self.y - 1), Pos(self.x - 1, self.y), Pos(self.x + 1, self.y), Pos(self.x, self.y + 1)]
        final = []
        for pos in temp:
            if pos.isValid():
                final.append(pos)
        return final


@dataclass
class Unit:
    ID: int
    pos: Pos
    t: str  # type
    hp: int
    attack: int


lines = pathlib.Path("inputs/15.txt").read_text().splitlines()
unitSet = frozenset({"G", "E"})

# Parse lines
Map = []
units = {}
curID = 0
for y, line in enumerate(lines):
    parsedLine = []
    for x, char in enumerate(line):
        if char in unitSet:
            pos = Pos(x, y)
            units[pos] = Unit(curID, pos, char, 200, 3)
            char = "."
            curID += 1
        parsedLine.append(char)
    Map.append(parsedLine)
initialUnits = copy.deepcopy(units)

# Run combat
elfAttack = 4
failed = True
numRound = 0
while failed:
    failed = False
    units = copy.deepcopy(initialUnits)
    for pos in units.keys():
        units[pos].hp = 200
        if units[pos].t == "E":
            units[pos].attack = elfAttack
    numRound = 0
    alive = {"E": sum([units[pos].t == "E" for pos in units.keys()]), "G": sum([units[pos].t == "G" for pos in units.keys()])}
    done = False
    while not done:
        canAttack = {units[pos].ID for pos in units}
        for pos in sorted(units.keys(), key=operator.attrgetter("y", "x")):
            if alive["E"] <= 0 or alive["G"] <= 0:
                done = True
            if pos not in units:  # has been killed
                continue
            unit = units[pos]
            if unit.ID not in canAttack:  # already attacked
                continue
            target = None
            for nearby in pos.getAround():
                if nearby not in units.keys():
                    continue
                nearbyUnit = units[nearby]
                if nearbyUnit.t != unit.t and (not target or nearbyUnit.hp < target.hp):
                    target = nearbyUnit

            if not target:  # Search for target
                alreadySearched = {pos}
                potential = collections.deque([{"nextPos": x, "searching": x} for x in pos.getAround()])
                while len(potential) > 0:
                    potentialPos = potential.popleft()
                    if potentialPos["searching"] in alreadySearched:
                        continue
                    alreadySearched.add(potentialPos["searching"])
                    if potentialPos["searching"] in units:
                        if unit.t != units[potentialPos["searching"]].t:
                            units[potentialPos["nextPos"]] = units.pop(unit.pos)
                            unit.pos = potentialPos["nextPos"]
                            for nearby in unit.pos.getAround():
                                if nearby not in units.keys():
                                    continue
                                nearbyUnit = units[nearby]
                                if nearbyUnit.t != unit.t and (not target or nearbyUnit.hp < target.hp):
                                    target = nearbyUnit
                            break
                    else:
                        potential.extend({"nextPos": potentialPos["nextPos"], "searching": x} for x in potentialPos["searching"].getAround())

            if target:  # Attack
                canAttack.remove(unit.ID)
                target.hp -= unit.attack
                if target.hp <= 0:
                    if target.t == "E":
                        failed = True
                        break
                    alive[target.t] -= 1
                    del units[target.pos]
        if done or failed:
            break
        numRound += 1
    elfAttack += 1

print(numRound * sum([units[pos].hp for pos in units.keys()]))
