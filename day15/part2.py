"""AoC_Year2015_Day15_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


import itertools, re

r_str = r"([A-Za-z]+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)"
ingredients = []
with open(INPUT_PATH, "r") as f:

    # while line := f.readline().strip():
    #     ingredients.append(re.findall(r_str, line))
    ingredients = re.findall(r_str, f.read())

# for i in ingredients:
#     print(i)


max_total_scores = 0


def get_sum_of_ingredients(teaspoons):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i, ingredient in enumerate(ingredients):
        a += int(ingredient[0 + 1]) * teaspoons[i]
        b += int(ingredient[1 + 1]) * teaspoons[i]
        c += int(ingredient[2 + 1]) * teaspoons[i]
        d += int(ingredient[3 + 1]) * teaspoons[i]
        e += int(ingredient[4 + 1]) * teaspoons[i]
    a = max(0, a)
    b = max(0, b)
    c = max(0, c)
    d = max(0, d)
    e = max(0, e)
    if e == 500:
        return a * b * c * d
    else:
        return 0


ma = 0
for combination in itertools.product(range(101), repeat=len(ingredients)):
    if sum(combination) == 100:
        ma = max(ma, get_sum_of_ingredients(combination))
    continue

print(ma)
