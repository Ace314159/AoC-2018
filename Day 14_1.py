import pathlib

numRecipes = int(pathlib.Path("inputs/14.txt").read_text().splitlines()[0])

recipes = [3, 7]
i, j = 0, 1
while len(recipes) < numRecipes + 10:
    newRecipe = map(int, list(str(recipes[i] + recipes[j])))
    recipes.extend(newRecipe)
    i = (i + 1 + recipes[i]) % len(recipes)
    j = (j + 1 + recipes[j]) % len(recipes)

print("".join(map(str, recipes[numRecipes:numRecipes + 10])))
