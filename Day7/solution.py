f = open('input.txt', 'r')
ls = [line.replace('bags', 'bag').split('bag')
      for line in f.read().splitlines()]
ls = [list(filter(lambda s: len(s) != 1, line)) for line in ls]
ls = [list(map(lambda s: s.replace(' contain', '').strip(',. '), line))
      for line in ls]




c_in = {line[0]: {bag[2:] for bag in line[1:]} for line in ls}
c_by ={line[0]: {key for key, value in c_in.items() if line[0] in value} for line in ls}
print(c_by)


contains_gold = set()

def check(colour):
    for cl in c_by[colour]:
        contains_gold.add(cl)
        check(cl)


check('shiny gold')
print(len(contains_gold))