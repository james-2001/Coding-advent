import numpy as np

f = open('input.txt', 'r')
ls = [line.split() for line in f.read().splitlines()]
ls = np.array([list(line[0]) for line in ls])



def iterate(start, n):
    while n > 0:
        new = start.append
        new =[]
        iterate(new, n-1)
    return
