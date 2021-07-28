f = open('input.txt', 'r')
ls = [line for line in f.read().splitlines()]
ls = [list(line) for line in ls]


def tree_counter(pair):
    across, up = pair
    tree_count = 0
    x_position, y_position = 0, 0
    while y_position < len(ls):
        line = ls[y_position]
        if line[x_position % (len(line))] == '#':
            tree_count += 1
        x_position += across
        y_position += up
    return tree_count


print(f'Part 1: {tree_counter((2,1))}')

inputs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

total = 1
for pair in inputs:
    total *= tree_counter(pair)

print(f'Part 2: {total}')
