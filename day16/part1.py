"""AoC_Year2015_Day16_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import re

r_str = r"Sue (\d+): ([A-Za-z]+): (\d+), ([A-Za-z]+): (\d+), ([A-Za-z]+): (\d+)"

valid_hm = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def check_aunt(aunt):
    compound1_name, compound1_value = aunt[1], int(aunt[2])
    compound2_name, compound2_value = aunt[3], int(aunt[4])
    compound3_name, compound3_value = aunt[5], int(aunt[6])
    if (
        valid_hm[compound1_name] == compound1_value
        and valid_hm[compound2_name] == compound2_value
        and valid_hm[compound3_name] == compound3_value
    ):
        return True
    return False


with open(INPUT_PATH, "r") as f:

    correct_aunt = "dfsf"
    for aunt_index, aunt in enumerate(re.findall(r_str, f.read()), start=1):

        # print(aunt_index)
        # # print(f"|{compound3_name}|")
        # print(compound1_name, compound1_value)
        # print(compound2_name, compound2_value)
        # print(compound3_name, compound3_value)
        # print()
        if check_aunt(aunt):
            print(aunt_index)

            break

    # print(correct_aunt)

    # print(aunt_index, compound1, compound2, compound3)
    # if valid_hm[compound1[0]] = compound1[]

    # while line := f.readline().strip():
    #     print(re.findall(r_str, line))
