f = open('input.txt', 'r')
ls = [line for line in f.read().splitlines()]
ls = [i.rsplit(' ') for i in ls]
n = len(ls)

bounds, letter, password = zip(*ls)
bounds = [i.rsplit('-') for i in bounds]
letter = [line[:-1] for line in letter]

correct_count_p1 = 0

for i in range(n):
    pw = password[i]
    char_count = pw.count(letter[i])
    if char_count >= int(bounds[i][0]) and char_count <= int(bounds[i][1]):
        correct_count_p1 += 1

print(correct_count_p1)

correct_count_p2 = 0

for i in range(n):
    pw = password[i]
    char = letter[i]
    low = int(bounds[i][0])
    up = int(bounds[i][1])
    if (pw[low-1] == char) != (pw[up-1] == char):
        correct_count_p2 += 1

print(correct_count_p2)
