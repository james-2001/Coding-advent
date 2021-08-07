f = open('input.txt', 'r')
ls = [line.replace('\n','') for line in f.read().split('\n\n')]

sum = 0
for group in ls:
    sum += len(set(group))

print(sum)
