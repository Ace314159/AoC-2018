import pathlib

seq = list(map(int, list(pathlib.Path("inputs/14.txt").read_text().splitlines()[0])))

recipes = [3, 7]
i, j = 0, 1
while True:
    newRecipe = list(map(int, list(str(recipes[i] + recipes[j]))))
    recipes.extend(newRecipe)
    i = (i + 1 + recipes[i]) % len(recipes)
    j = (j + 1 + recipes[j]) % len(recipes)
    if recipes[-len(seq):] == seq:
        print(len(recipes) - len(seq))
        break
    if len(newRecipe) == 2 and recipes[-len(seq) - 1:-1] == seq:
        print(len(recipes) - len(seq) - 1)
        break
