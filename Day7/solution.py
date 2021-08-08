f = open('test.txt', 'r')
ls = [line.replace('bags', 'bag').split('bag')
      for line in f.read().splitlines()]
ls = [list(filter(lambda s: len(s) != 1, line)) for line in ls]
ls = [list(map(lambda s: s.replace(' contain', '').strip(',. '), line))
      for line in ls]


bags = {line[0]: {bag[2:]: bag[0] for bag in line[1:]} for line in ls}




def contains(colour):
      contain_set = {colour}
      for key, value in bags.items():
            inters = contain_set.intersection(set(value.keys()))
            if inters:
                  contain_set.add(key)              
      return contain_set

# if 'shiny gold' not in list(bags['shiny gold'].keys()):
#       contain_set.remove('shiny gold')


# print((contain_set))
