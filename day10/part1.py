"""AoC_Year2015_Day10_Part1"""

INPUT_PATH = "input.txt"
EXAMPLE_INPUT_PATH = "example6.txt"


with open(INPUT_PATH, "r") as f:
    # while line := f.readline().strip():
    line = f.read().strip()
    # line = "22211333"
    # print(line)

    for i in range(40):
        line += "T"
        index = 0
        freqs = []
        while index <= len(line) - 1:
            element_counter = 0
            # len(line) - 1
            for second_index in range(index, len(line)):
                # print(
                #     line[index],
                #     f"first:{index}",
                #     f"second:{second_index}",
                #     f"          {second_index+1}  {len(line)}",
                # )
                if line[second_index] == line[index] and second_index != "T":
                    element_counter += 1
                else:
                    # print(line[index], element_counter)
                    freqs.append((line[index], element_counter))
                    index = second_index - 1
                    break
            #     print("s", line[second_index])
            index += 1

        line = "".join([f"{freq}{char}" for char, freq in freqs])

    # for char, freq in freqs:
    #     print(char, freq)
    # print(("".join([f"{freq}{char}" for char, freq in freqs])))
    print(len(line))
