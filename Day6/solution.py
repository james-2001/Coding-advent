f = open('input.txt', 'r')
ls = [line for line in f.read().split('\n\n')]

p1_ls = [line.replace('\n', '') for line in ls]

count = 0
for group in p1_ls:
    count += len(set(group))

print(f'Part 1: {count}')

p2_ls = [line.split('\n') for line in ls]
p2_ls = [list(filter(bool, line)) for line in p2_ls]

p2_count = 0
for group in p2_ls:
    shared = group[0]
    for person in group[1:]:
        shared = ''.join(set(person).intersection(shared))
    if len(shared) != 0:
        p2_count += len(shared)

print(f'Part 2: {p2_count}')
