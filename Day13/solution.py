from operator import sub, imod
from functools import reduce

f = open("input.txt")
time, buses_full = [line for line in f.read().splitlines()]
time = int(time)
bus = list(filter(lambda s: s != "x", buses_full.split(",")))
bus = list(map(int, bus))

for i in range(max(bus)):
    time_stamp = time + i
    if any([time_stamp % bus_no == 0 for bus_no in bus]):
        x = [i * bus_no for bus_no in bus if time_stamp % bus_no == 0].pop()
        print(f'Part 1: {x}')
        break


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


a1 = [(buses_full.split(",")).index(str(number)) for number in bus]
a1 = list(map(sub, bus, a1))
a1 = list(map(imod, a1, bus))
print(f'Part 2: {chinese_remainder(bus,a1)}')
