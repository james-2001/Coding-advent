"""
Not working: too slow
"""

import numpy as np
import itertools as it

f = open("input.txt", "r")
rules, msg = [line.split("\n") for line in f.read().split('\n\n')]
rules = [line.split(":") for line in rules]
rules = sorted(rules, key=lambda s: int(s[0]))
rules = [line[1].strip(" \"").split(" | ") for line in rules]
rules = [[i.split() for i in line] for line in rules]

count = len(list(filter(lambda s: len(s)== 2 , rules)))
paths = list(it.product(*[(0,1) for _ in range(count)]))
rules_split=[]

for path in paths:
    ts=rules.copy()
    path=list(path)
    for j in range(len(rules)):
        if len(ts[j])==2:
            x = path.pop()
            ts[j] = ts[j][x]
        else:
            ts[j] = ts[j][0]
    rules_split.append(ts)

def build(st, rule, pointer):
    pointer = int(pointer)
    if not rule[pointer][0].isdigit():
        return st + rule[pointer][0]
    else:
        for i in rule[pointer]:
            st = build(st, rule, i) 
        return st
print("done!")
allowed =set()
for i in rules_split:
    allowed.add(build("", i, 0))

print(allowed)

print(len(list(filter(lambda s: s in allowed, msg))))

