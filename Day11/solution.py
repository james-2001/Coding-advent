import numpy as np
from scipy import ndimage as sp

f = open("input.txt", "r")
ls = np.array([line for line in f.read().splitlines()])
floor = np.array([list(map(lambda s: 1 if s == "." else 0, line))
                  for line in ls])
start = np.zeros(floor.shape, dtype=int)

convolve_array = np.ones((3, 3), dtype=int)
convolve_array[1, 1] = 0


def cycle(state):
    state_neigbours = sp.convolve(state, convolve_array,
                                  mode='constant', cval=0)
    state = (((state == 0) & (state_neigbours == 0)) | ((state == 1) & (
               state_neigbours < 4))) & (floor != 1)
    state = np.array([list(map(int, line)) for line in state])
    return state


def cycle_to_end():
    prev = start
    while not (prev == cycle(prev)).all():
        prev = cycle(prev)
    return prev


print(f'Part 1: {np.sum(cycle_to_end())}')
