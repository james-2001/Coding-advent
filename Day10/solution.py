input_file = [int(line) for line in open("input.txt", "r").read().splitlines()]
adapters = sorted(input_file + [0, max(input_file)+3])
diffs = [adapters[i+1]-adapters[i] for i in range(len(adapters)-1)]

print(f'Part 1: {diffs.count(1)*diffs.count(3)}')

memo = {}


def count(i):
    if i == len(adapters)-1:
        return 1
    if i in memo:
        return memo[i]
    a = sum([count(j) if adapters[j]-adapters[i] <= 3 else 0
             for j in range(i+1, len(adapters))])
    memo[i] = a
    return a


print(f'Part 2: {count(0)}')
