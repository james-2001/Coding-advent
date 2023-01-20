from collections import defaultdict

with open("2022/Day14/input.txt") as f:
    lines = f.read().splitlines()

s = [[tuple(map(int, x.split(","))) for x in i.split("->")] for i in lines]

grid = defaultdict(lambda: 0)

for rock in s:
    for (sx,sy), (ex,ey) in zip(rock,rock[1:]):
        if sx == ex:
            while sy!=ey:
                dir = (ey-sy)/abs(ey-sy)
                grid[sx, sy] = -1
                sy += dir
        else:
            while sx!=ex:
                dir = (ex-sx)/abs(ex-sx)
                grid[sx, sy]=-1
                sx +=dir
        grid[ex,ey]=-1

height = max(y for (_,y) in grid.keys())

for x in range(-1000,1000):
    grid[x, height+2] = -1

start = (500,0)
sx, sy = start

def drop_sand(cx,cy, pt1 = True):
    if cy>height and pt1:
        return False
    for x,y in ((0,1), (-1,1), (1,1)):
        if grid[(cx+x,cy+y)] == 0:
            return drop_sand(cx+x,cy+y, pt1)
    grid[cx,cy] = 1
    return True
            
    

while drop_sand(sx,sy):
    drop_sand(sx,sy)
    
print(sum(x for x in grid.values() if x==1))

while grid[500,0]==0:
    drop_sand(sx,sy, False)
    
print(sum(x for x in grid.values() if x==1))


