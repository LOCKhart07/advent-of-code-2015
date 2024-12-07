"""AoC_Year2015_Day5_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import re


r_str = r"ab|cd|pq|xy"


def check_line(line):
    repeat_once_flag = False
    pairs_flag = False

    for i in range(len(line)):
        if i + 1 < len(line):
            pair = line[i] + line[i + 1]
            string_to_check_in = line[:i] + "  " + line[i + 2 :]

            # print(string_to_check_in)
            if pair in string_to_check_in:
                # print(pair)
                pairs_flag = True

        window = line[i - 1 : i + 2]
        if len(window) == 3:
            # print([i for i in window])
            if window[0] == window[2]:
                repeat_once_flag = True

    return repeat_once_flag and pairs_flag


nice_counter = 0
with open(INPUT_PATH, "r") as f:
    while line := f.readline():
        # print(f"{line.strip()}")
        # result = check_line(line.strip())

        # print(result)
        # print()
        # print(line.strip())
        # check_line(line.strip())
        if check_line(line.strip()):
            nice_counter += 1
        # print()

print(nice_counter)
