"""AoC_Year2015_Day8_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    str_literals = 0
    encoded_chars = 0
    while line := f.readline().strip():
        str_literals += len(line)
        encoded_line = '"' + line.replace("\\", "\\\\").replace('"', r"\"") + '"'
        # print(f"{line}-----------{encoded_line}")
        encoded_chars += len(encoded_line)
        # print()
        # print(line, len(line))
        # print()

print(encoded_chars - str_literals)
