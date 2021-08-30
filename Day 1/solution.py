from numpy import polynomial as pn
from math import factorial

temp = []
with open('input.txt','r') as stream:
    for line in stream:
        temp.append(line)
        data = [line[:-1] for line in temp]
data = [int(i) for i in data]

# Solution 1


n = len(data)
for i in range(n):
    for j in range(i+1,n):
        if data[i] + data[j] == 2020:
            print(f'Part 1: {data[i]*data[j]}')
        for k in range(j+1,n):
            if data[i]+data[j]+data[k] == 2020:
                print(f'Part 2: {data[i]*data[j]*data[k]}')


# Solution 2: Generating functions


p = pn.Polynomial([0]*2020)
for i in data:
    p.coef[i] = i

print(f'Part 1: {(p**2).coef[2020]/factorial(2)}')
print(f'Part 2: {(p**3).coef[2020]/factorial(3)}')
