from functools import cmp_to_key

with open("2022/Day13/input.txt") as f:
    inp = f.read().split("\n\n")

ins = map(lambda s: s.splitlines(), inp)
ins = list(map(lambda x: tuple(map(eval, x)), ins))

def comp_vals(left, right):
    match left, right:
        case int(), int():
            return   (left < right) -(left > right )
        case list(), int():
            return comp_vals(left, [right])
        case int(), list():
            return comp_vals([left], right)
        case list(), list():
            for (a,b) in zip(left, right):
                if a!=b:
                    return comp_vals(a,b)
            return (len(left) < len(right)) - (len(left) > len(right)) 


x=list(map(lambda pair: comp_vals(*pair), ins))
print(x)
print(sum([i+1 for i in range(len(x)) if x[i] ==1 ]))

flattened_ins = [i for sublist in ins for i in sublist] + [[[2]], [[6]]]
sorted_packets = list(reversed(sorted(flattened_ins,key=cmp_to_key(comp_vals))))


print((sorted_packets.index([[2]]) +1) * (sorted_packets.index([[6]])+1))