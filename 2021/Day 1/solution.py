with open("2021/Day1/input.txt") as f:
    depths = list(map(int, f.read().splitlines()))

count1 = [depths[i-1] < depths[i] for i in range(1, len(depths))]
count2 = [sum(depths[i:i+3]) < sum(depths[i+1:i+4])
          for i in range(len(depths))]


print(sum(count1), sum(count2))
