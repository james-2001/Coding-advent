f = open('input.txt', 'r')
ls = [int(line) for line in f.read().splitlines()]


def is_sum_of(ls, target):
    s = set(ls)
    sum_list = [(target - i) in s for i in ls]
    return any(sum_list)


def attack(pa, data):
    for i in range(pa, len(data)):
        if not is_sum_of(data[i-pa:i], data[i]):
            return data[i]


weakness = attack(25, ls)


def exploit(val, data):
    for i in range(len(data)):
        acc = []
        j = 0
        while sum(acc) < val:
            acc = data[i:i+j]
            j += 1
            if sum(acc) == val:
                return min(acc)+max(acc)


print(f'Part 1: {weakness}')
print(f'Part 2: {exploit(weakness, ls)}')
