from operator import add
import itertools as it

f = open('input.txt', 'r')
ls = [line for line in f.read().splitlines()]
ls = [list(map(lambda s: s.strip(), line.split("="))) for line in ls]


mem = {}
current_mask = 0


def mask1(value, mask):
    value = list(expand(bin(value)[2:]))
    mask = map(lambda s: "" if s == "X" else s, list(mask))
    masked_val = map(add, mask, value)
    masked_val = map(lambda s: s[0], masked_val)
    return int(''.join(masked_val), 2)


def mask2(value, mask):
    value = list(expand(bin(value)[2:]))
    mask = map(lambda s: "" if s == "0" else s, list(mask))
    masked_val = map(add, mask, value)
    masked_val = list(map(lambda s: s[0], masked_val))
    adresses = replace_x("".join(masked_val))
    return adresses


def expand(val):
    while len(val) < 36:
        val = "0" + val
    return val


def replace_x(st):
    count = st.count("X")
    possiblities = []
    replacements = map(list, it.product([0, 1], repeat=count))
    for vals in replacements:
        possiblities.append([str(vals.pop()) if c == 'X' else c for c in st])
    return list(map(lambda s: int("".join(s), 2), possiblities))


for instruction, value in ls:
    if instruction == 'mask':
        current_mask = value
    if instruction.startswith('mem'):
        mem[instruction[4:-1]] = mask1(int(value), current_mask)

print(f'Part 1: {sum(mem.values())}')

mem = {}
for instruction, value in ls:
    if instruction == 'mask':
        current_mask = value
    if instruction.startswith('mem'):
        for i in mask2(int(instruction[4:-1]), current_mask):
            mem[i] = value

print(f'Part 2: {sum(map(int, mem.values()))}')
