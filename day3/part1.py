'''AoC_Year2015_Day3_Part1'''



INPUT_PATH=r"input.txt"
EXAMPLE_INPUT_PATH=r"example1.txt"



INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


with open(INPUT_PATH, "r") as f:
    directions = f.read()


matrix = {}

starting_location = (0, 0)

santa_location = (0, 0)
matrix[santa_location] = 1

direction_map = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
for direction in directions:
    x = santa_location[0] + direction_map[direction][0]
    y = santa_location[1] + direction_map[direction][1]
    santa_location = (x, y)

    current_visited_value = matrix.get(santa_location, 0)

    matrix[santa_location] = current_visited_value + 1

    # print(santa_location)

# print(directions)
print(len(matrix))