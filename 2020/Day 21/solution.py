import re

with open("test.txt", "r") as f:
    lines = [re.sub(r'([(),])', "", line).split(" contains ") for line in f.read().splitlines()]
print(lines)