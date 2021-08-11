f = open('input.txt', 'r')
ls = [line.replace('no', '0').replace('bags', 'bag').split('bag')
      for line in f.read().splitlines()]
ls = [list(filter(lambda s: len(s) != 1, line)) for line in ls]
ls = [list(map(lambda s: s.replace(' contain', '').strip(',. '), line))
      for line in ls]

c_in = {line[0]: {(bag[2:], bag[0]) for bag in line[1:]} for line in ls}
c_by = {line[0]: {key for key, value in c_in.items()
        if line[0] in [pair[0] for pair in value]}
        for line in ls}
print(c_in)


contains_gold = set()
total_cost = 0


def check(colour):
    for cl in c_by[colour]:
        contains_gold.add(cl)
        check(cl)


def cost(colour, count):
    global total_cost
    if colour == 'other':
        return
    for cl in c_in[colour]:
        total_cost += count*int(cl[1])
        cost(cl[0], count*int(cl[1]))


check('shiny gold')
print(cost('shiny gold', 1))
print(f'part 1: {len(contains_gold)}')
print(f'part 2: {total_cost}')
