import numpy as np
import itertools as it

with open("input.txt", "r") as f:
    lines = {int(lines[0][5:9]): list(map(lambda s: list(s.replace('#','1').replace('.','0')), lines[1:])) 
             for lines in map(lambda s: s.splitlines(), f.read().split("\n\n"))}


def rotate_flip(arr):
    arr2=[]
    for _ in range(4):
        arr2 +=[list(arr[0]), list(reversed(arr[0]))]
        arr = np.rot90(arr)
    return arr2

all_edges = set()
edges={}
for key, tile in lines.items():
    tile_edges = rotate_flip(tile)
    edges[key] =tile_edges

acc=1
for key, edge in edges.items():
    others = [i for t_key, i in edges.items() if t_key!= key]
    others = list(it.chain(*others))
    unique_edges = sum([i in others for i in edge])/2
    if unique_edges ==2:
        acc*=key

print(acc) 