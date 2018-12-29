import pathlib
import operator

lines = pathlib.Path("inputs/13.txt").read_text().splitlines()
dirs = set(["^", "v", "<", ">"])
yDirs = set(["^", "v"])
plusDirs = set(["v", ">"])
changeDir = {"x": "y", "y": "x"}
changeOp = {operator.add: operator.sub, operator.sub: operator.add}
interChange = ["y", None, "x"]

rails = []
carts = []
occupied = {}
for y, line in enumerate(lines):
    lineL = list(line)
    for x, char in enumerate(lineL):
        if char in dirs:
            if char in yDirs:
                direction = "y"
                lineL[x] = "|"
            else:
                direction = "x"
                lineL[x] = "-"
            if char in plusDirs:
                op = operator.add
            else:
                op = operator.sub
            carts.append({"x": x, "y": y, "dir": direction, "op": op, "inter": 0})
            occupied[(x, y)] = True

    rails.append(lineL)

while True:
    carts.sort(key=operator.itemgetter("y", "x"))
    done = False
    for cart in carts:
        del occupied[(cart["x"], cart["y"])]
        cart[cart["dir"]] = cart["op"](cart[cart["dir"]], 1)
        curPos = (cart["x"], cart["y"])
        if curPos in occupied:
            print(cart["x"], cart["y"], sep=",")
            done = True
            break
        else:
            occupied[curPos] = True

        track = rails[cart["y"]][cart["x"]]
        if track == "/":
            cart["dir"] = changeDir[cart["dir"]]
            cart["op"] = changeOp[cart["op"]]
        elif track == "\\":
            cart["dir"] = changeDir[cart["dir"]]  # op stays the same
        elif track == "+":
            if cart["inter"] != 1:
                cart["dir"] = changeDir[cart["dir"]]
                if cart["dir"] == interChange[cart["inter"]]:
                    cart["op"] = changeOp[cart["op"]]
            cart["inter"] = (cart["inter"] + 1) % 3
    if done:
        break
