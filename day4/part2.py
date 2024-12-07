"""AoC_Year2015_Day4_Part2"""

INPUT_PATH = r"input.txt"
EXAMPLE_INPUT_PATH = r"example1.txt"


with open(INPUT_PATH, "r") as f:
    secret_key = f.read()

import hashlib

i = 0
while True:
    i += 1
    s = secret_key + str(i)
    md5_hash = hashlib.md5(s.encode("utf-8")).hexdigest()
    if md5_hash[:6] == "000000":
        print(i)
        break
#     hashes.append(md5_hash)

# print(hashes)
