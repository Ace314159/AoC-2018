import pathlib


data = map(int, pathlib.Path("inputs/8.txt").read_text().splitlines()[0].split(" "))
metadataSum = 0


def buildNode():
    global metadataSum
    node = {"children": [], "metadata": [], "metadataSum": 0}
    numChildren = next(data)
    numMetadata = next(data)
    for _ in range(numChildren):
        node["children"].append(buildNode())
    for _ in range(numMetadata):
        node["metadata"].append(next(data))
        metadataSum += node["metadata"][-1]
    return node


buildNode()
print(metadataSum)
