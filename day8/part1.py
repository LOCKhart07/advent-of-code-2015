"""AoC_Year2015_Day8_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    str_literals = 0
    actual_chars = 0
    while line := f.readline().strip():
        str_literals += len(line)
        actual_chars += len(eval(line))
        # print()
        # print(line, len(line))
        # print()

print(str_literals - actual_chars)
