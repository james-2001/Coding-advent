
with open("input.txt", "r") as f:
    me, crab = [list(map(int, lines.splitlines()[1:])) for lines in f.read().split("\n\n")]

def game(p1: list, p2: list, part1: bool = False):
    while p1 and p2:
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if c1 > c2:
            p1+=[c1,c2]
        else:
            p2+=[c2,c1]
    if part1:
        print(score(max(p1, p2, key=len)))
    return bool(p1) 

def score(deck):
    n= len(deck)
    return sum([deck[n-i]*i for i in range(1, n+1)])


def recurse(p1, p2):
    previous = set()
    while p1 and p2:
        if (tuple(p1),tuple(p2)) in previous:
            return True
        previous.add((tuple(p1),tuple(p2)))
        c1 = p1.pop(0)
        c2 = p2.pop(0)
        if len(p1) >= c1 and len(p1) >= c2:
            winner = recurse(p1[:c1], p2[:c2])
        else:
            winner = c1>c2 
        if winner:
            p1 += [c1, c2]
        else:
            p2 += [c2, c1]
    return len(p1)>len(p2)

print(me,crab)
recurse(me, crab)
print(me, crab)
print(sum((i+1)*v for i,v in enumerate(me[::-1])))