import numpy as np

with open("2022/Day12/input.txt") as f:
    x = f.read().splitlines()

inp = np.array(list(map(list,x)))

starting = (np.where(inp=='S')[0][0], np.where(inp=='S')[1][0])
final = (np.where(inp=='E')[0][0], np.where(inp=='E')[1][0])

def conv_char_to_int(c):
    if c == 'S':
        return 0
    if c =='E':
        return ord('z')- ord('a')
    return ord(c)-ord('a')

converted_input = np.vectorize(conv_char_to_int)(inp)

def bfs(in_mat: np.ndarray, start: tuple, part2: bool = False) -> int:
    q = [start]
    distances = np.zeros_like(in_mat)
    sizex, sizey = in_mat.shape
    check= [(0,1),(1,0),(-1,0),(0,-1)]
    while q:
        cx, cy = q.pop(0)
        current_dist = distances[cx,cy]
        for nx, ny in check:
            ax = nx + cx
            ay = ny + cy
            if (0<= ax < sizex and 0 <=ay<sizey ) and distances[ax,ay] == 0:
                if ((not part2) and in_mat[ax,ay] - in_mat[cx,cy] < 2) or (part2 and in_mat[cx,cy]-in_mat[ax,ay] < 2):
                    distances[ax,ay] = 1 + current_dist
                    q = q+[(ax,ay)]
    return distances

print(bfs(converted_input, starting)[final])

lowest_spots = np.where(converted_input == 0)
lowest_spots = [(lowest_spots[0][i], lowest_spots[1][i]) for i in range(len(lowest_spots[0]))]

search = bfs(converted_input, final, True)
walking_distance = [search[i] for i in lowest_spots if search[i]>0]


print(min(walking_distance))