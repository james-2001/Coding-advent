from itertools import product
from collections import defaultdict

with open("/home/james/Coding-advent/2022/Day15/test.txt") as f:
    lines = f.read().splitlines()

def empty_space(x):
    return list(filter(lambda a: a[0]+a[1] <= x, product(range(x+1), range(x+1))))

sensors = []

for i in lines:
    i+="."
    x=list(map(lambda y: int(y[2:-1]),[x for x in i.split(" ") if "=" in x]))
    x = [(x[0],x[1]),(x[2],x[3])]
    sensors.append(x)

grid = defaultdict(lambda:0)

for (sx,sy), (bx,by) in sensors:
    distance = (sx-bx) + (sy-by)
    for (x,y) in empty_space(distance):
        grid[sx+x,sx+y]=1
        grid[sx-x,sx-y]=1
        grid[sx+x,sx-y]=1
        grid[sx-x,sx+y]=1

print(([(a,b) for (a,b) in grid.keys() if b ==10]))
