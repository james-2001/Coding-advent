with open("2022/Day10/test.txt") as f:
    inp = f.read().splitlines()

print([20+(40*i) for i in range(6)])

acc = 0
prev = [0,0]
cycle = 0

for x in inp:
    cycle+=1
    if cycle in [20+(40*i) for i in range(6)]:
        print(acc)
    acc+=prev.pop(0)
    if x.startswith("noop"):
        prev.append(0)
    else:
        prev.append(int(x[5:]))
print(cycle)
