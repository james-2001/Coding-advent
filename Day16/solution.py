import itertools as it

f = open('input.txt', 'r')
fields, ticket, nearby = [line.split("\n") for line in f.read().split("\n\n")]

fields = [line.split(':') for line in fields]
fields = {line[0]: [tuple(vals.split("-")) for vals in
          line[1].replace(" ", "").split("or")] for line in fields}

ticket = list(map(int, [line.split(",") for line in ticket][1]))

nearby = [line.split(",") for line in nearby]
nearby = filter(lambda s: len(s) != 1, nearby)
nearby = list(map(lambda s: [int(i) for i in s], nearby))

valid_set = set()
for ranges in fields.values():
    range_0 = list(map(int, ranges[0]))
    range_1 = list(map(int, ranges[1]))
    valid_set = valid_set.union({i for i in range(range_0[0], range_0[1]+1)})
    valid_set = valid_set.union({i for i in range(range_1[0], range_1[1]+1)})

all_nearby = list(it.chain(*nearby))
tser = sum(filter(lambda s: s not in valid_set, all_nearby))
print(f'Part 1: {tser}')
