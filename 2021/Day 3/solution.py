import numpy as np

with open("2021/Day 3/input.txt") as f:
    report = f.read().splitlines()

report = np.array(list(map(lambda s: list(map(int, list(s))), report)))
bitsum = np.sum(report, axis=0)
gamma = ["1" if s > 0.5*report.shape[0] else "0" for s in bitsum]
epsilon = ["1" if s < 0.5*report.shape[0] else "0" for s in bitsum]


print(int("".join(gamma), base = 2)*int("".join(epsilon), base = 2))
