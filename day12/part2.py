"""AoC_Year2015_Day12_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


import json, re


def get_sum(obj, current_sum):
    if isinstance(obj, dict):
        running_sum = 0
        for key in obj:
            if obj[key] == "red":
                break
            running_sum += get_sum(obj[key], current_sum)
        else:
            return current_sum + running_sum
        return current_sum
    elif isinstance(obj, list):
        running_sum = 0
        for item in obj:
            running_sum += get_sum(item, current_sum)
        return current_sum + running_sum
    elif isinstance(obj, int):
        return current_sum + obj
    else:
        return current_sum
    print()


with open(INPUT_PATH, "r") as f:
    json_obj = json.load(f)

    sumo = get_sum(json_obj, 0)

    print(sumo)
