"""AoC_Year2015_Day1_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


floor = 0
with open(INPUT_PATH, "r") as f:
    while line := f.readline():
        for char in line:
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1

print(floor)
