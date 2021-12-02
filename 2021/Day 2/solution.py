with open("2021/Day 2/input.txt") as f:
    instructions = f.read().splitlines()
instructions = list(map(lambda s: s.split(), instructions))

total = [0, 0]
for line in instructions:
    if line[0] == "forward":
        total[0] += int(line[1])
    elif line[0] == "down":
        total[1] += int(line[1])
    elif line[0] == "up":
        total[1] -= int(line[1])

print(total[0]*total[1])

aim = 0
total = [0, 0]
for line in instructions:
    if line[0] == "forward":
        total[0] += int(line[1])
        total[1] += aim*int(line[1])
    if line[0] == "down":
        aim += int(line[1])
    if line[0] == "up":
        aim -= int(line[1])
print(total[0]*total[1])
