from math import prod

with open("input.txt", "r") as f:
    p1, p2 = [list(map(int, lines.splitlines()[1:])) for lines in f.read().split("\n\n")]

while p1 and p2:
    c1 = p1.pop(0)
    c2 = p2.pop(0)
    if c1 > c2:
        p1+=[c1,c2]
    else:
        p2+=[c2,c1]

def score(deck):
    n= len(deck)
    return sum([deck[n-i]*i for i in range(1, n+1)])

print(score(max(p1,p2, key=len)))