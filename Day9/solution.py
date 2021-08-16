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


print(attack(25, ls))
