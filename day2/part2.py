"""AoC_Year2015_Day2_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

s = 0
with open(INPUT_PATH, "r") as f:
    while line := f.readline():
        sides = [int(i) for i in line.strip().split("x")]
        smallest_sides = sorted(sides)[:-1]
        sa = (smallest_sides[0] + smallest_sides[1]) * 2 + (
            sides[0] * sides[1] * sides[2]
        )
        # print(sides, "          ", sa)
        s += sa


print(s)
