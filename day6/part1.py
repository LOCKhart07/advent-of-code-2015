"""AoC_Year2015_Day6_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


def follow_instruction(instruction, current_status):
    if instruction == "turn on":
        return True
    elif instruction == "turn off":
        return False
    elif instruction == "toggle":
        return not current_status


grid = {}

on_lights = set()
# for y in range(10000):
#     for x in range(10000):
#         grid[(x, y)] = False


with open(INPUT_PATH, "r") as f:
    while line := f.readline().strip():
        # print(line)
        if line.startswith("turn on"):
            instruction = "turn on"
        elif line.startswith("toggle"):
            instruction = "toggle"
        elif line.startswith("turn off"):
            instruction = "turn off"
        start, end = map(
            lambda a: a.strip().split(","),
            line[len(instruction) :].split("through"),
        )
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))

        for y in range(start[1], end[1] + 1):
            for x in range(start[0], end[0] + 1):
                current_status = True if (x, y) in on_lights else False
                # print(instruction)
                if follow_instruction(instruction, current_status):
                    on_lights.add((x, y))
                else:
                    try:
                        on_lights.remove((x, y))
                    except KeyError:
                        pass


# on_counter = 0
# for coord in grid:
#     if grid[coord]:
#         on_counter += 1

print(len(on_lights))
