"""AoC_Year2015_Day5_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"

import re


r_str = r"ab|cd|pq|xy"


def check_line(line):
    vowel_counter = 0

    last_letter = ""
    last_letter_flag = False
    for char in line:
        if char == last_letter:
            last_letter_flag = True
        else:
            last_letter = char
        if char in "aeiou":
            vowel_counter += 1

    if vowel_counter < 3 or not last_letter_flag:
        # print(vowel_counter)
        return False

    if re.findall(r_str, line):
        return False
    return True


nice_counter = 0
with open(INPUT_PATH, "r") as f:
    while line := f.readline():
        # print(line)
        if check_line(line):
            nice_counter += 1

print(nice_counter)
