with open("2022/Day9/test.txt") as f:
    input = f.read().splitlines()

instructions = list(map(lambda x: x.split(" "), input))

head = (0,0)
tail = (0,0)

def calculate_tail(head, tail):
    distance = [head[0]-tail[0], head[1]-tail[1]]

for move in instructions:
    match move[0]:
        case 'R':
            head[0] += move[2]
        case 'U':
            head[1] += move[2]
        case 'L':
            head[0] -= move[2]
        case 'D':
            head[1] -= move[2]
