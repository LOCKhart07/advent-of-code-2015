"""AoC_Year2015_Day6_Part2"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example1.txt"


def follow_instruction(instruction, current_status):
    if instruction == "turn on":
        return current_status + 1
    elif instruction == "turn off":
        return current_status - 1 if current_status > 0 else 0
    elif instruction == "toggle":
        return current_status + 2


grid = {}

lights_status = {}
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
                # current_status = True if (x, y) in on_lights else False
                current_status = lights_status.get((x, y), 0)

                lights_status[(x, y)] = follow_instruction(instruction, current_status)


t_brightness = 0
for coord in lights_status:
    t_brightness += lights_status[coord]

print(t_brightness)
