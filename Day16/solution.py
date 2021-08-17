import numpy as np
import itertools as it
import math
from numpy.lib.shape_base import column_stack

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
    valid_set = valid_set.union(set(range(range_0[0], range_0[1]+1)))
    valid_set = valid_set.union(set(range(range_1[0], range_1[1]+1)))

all_nearby = list(it.chain(*nearby))
tser = sum(filter(lambda s: s not in valid_set, all_nearby))
print(f'Part 1: {tser}')

correct_nearby = np.array(list(filter(lambda s: all([i in valid_set for i in s]),
                          nearby)))
correct_nearby = np.insert(correct_nearby, 0, ticket, axis=0)
correct_nearby = correct_nearby.transpose()

field_ticket = {i: set() for i in fields.keys()}

for column in correct_nearby:
    for key, (range1, range2) in fields.items():
        range1 = tuple(map(int, range1))
        range2 = tuple(map(int, range2))
        possible = set(range(range1[0], range1[1]+1)).union(set(range(range2[0], range2[1]+1)))
        if set(column).issubset(possible):
            field_ticket[key].add(column[0])

sorted_fields = sorted(field_ticket, key= lambda i: len(field_ticket[i]))
acc, used = [], set()

for field in sorted_fields:
    if field.startswith('departure'):
        acc.append((field_ticket[field]-used).pop())
    used.update(field_ticket[field])

print(acc)

"""
This drove me up the wall
- Needs linting and neatening
- Python wont compute the product, but will if you hard code values and product of that list
"""
