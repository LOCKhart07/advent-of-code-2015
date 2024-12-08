"""AoC_Year2015_Day12_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


import json, re

NUMBER_REGEX = r"-*\d+"

with open(INPUT_PATH, "r") as f:
    # js = json.load(f)
    text = f.read()


print(sum([int(i) for i in re.findall(NUMBER_REGEX, text)]))
# print(json.dumps(js, indent=4))
