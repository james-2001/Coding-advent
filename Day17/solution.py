import numpy as np
from scipy import ndimage as sp

f = open('input.txt', 'r')
ls = [list(line.replace('#', '1').replace('.', '0'))
      for line in f.read().splitlines()]
ls = np.array([list(map(int, line)) for line in ls])


def cycles(state, dim, n):
    state = np.expand_dims(state, axis=tuple(range(dim-2)))

    convolve_array = np.ones((3,)*dim)
    convolve_array[(1,)*dim] = 0

    for _ in range(n):
        state = np.pad(state, 1).astype(int)
        neigbour_count = sp.convolve(state, convolve_array,
                                     mode='constant', cval=0.0)
        state = (((state == 1) & ((neigbour_count == 3) | (neigbour_count == 2)))
                 | ((state == 0) & (neigbour_count == 3)))
    return np.sum(state)


print(f'Part 1: {cycles(ls,3,6)}')
print(f'Part 2: {cycles(ls,4,6)}')
