with open("2022/Day5/input.txt") as f:
    input = f.read()
    starting_crates, instructions = input.split("\n\n") 

starting_crates = starting_crates.splitlines()[:-1]

def reverseAndReturn(x):
    x.reverse()
    return x

def parse_line(s: str):
    return [list(s)[i] for i in range(len(s)) if i%4==1]

def parse_instructions(s: str):
    words = s.split(" ")
    return list(map(int, [words[1], words[3], words[5]]))

starting_crates = list(map(parse_line, starting_crates))
crates = [reverseAndReturn([line[i] for line in starting_crates if line[i]!=" "]) for i in range(len(starting_crates[0]))]


movements = [parse_instructions(x) for x in instructions.splitlines()]
for move in movements:
    for _ in range(move[0]):    
        current = crates[move[1]-1].pop()
        crates[move[2]-1].append(current)

print("".join([c[-1] for c in crates]))

crates = [reverseAndReturn([line[i] for line in starting_crates if line[i]!=" "]) for i in range(len(starting_crates[0]))]
for move in movements:
    current = crates[move[1]-1][-(move[0]):]
    crates[move[1]-1] = crates[move[1]-1][:-(move[0])]
    crates[move[2]-1].extend(current)

print("".join([c[-1] for c in crates]))
