import pathlib


data = map(int, pathlib.Path("inputs/8.txt").read_text().splitlines()[0].split(" "))


def buildNode():
    global metadataSum
    node = {"children": [], "metadata": [], "metadataSum": 0}
    numChildren = next(data)
    numMetadata = next(data)
    for _ in range(numChildren):
        node["children"].append(buildNode())
    for _ in range(numMetadata):
        node["metadata"].append(next(data))
        node["metadataSum"] += node["metadata"][-1]
    return node


def getValue(node):
    if len(node["children"]) == 0:
        return node["metadataSum"]
    valueSum = 0
    for val in node["metadata"]:
        if 1 <= val <= len(node["children"]):
            valueSum += getValue(node["children"][val - 1])
    return valueSum


print(getValue(buildNode()))
