"""AoC_Year2015_Day1_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


def solve():
    floor = 0
    index = 0
    with open(INPUT_PATH, "r") as f:
        while line := f.readline():
            for char in line:
                if char == "(":
                    floor += 1
                    index += 1
                elif char == ")":
                    floor -= 1
                    index += 1

                if floor < 0:
                    print(index)
                    return


solve()
