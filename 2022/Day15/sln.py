with open("2022/Day15/test.txt") as f:
    lines = f.read().splitlines()

sensors = []

for i in lines:
    i+="."
    x=list(map(lambda y: int(y[2:-1]),[x for x in i.split(" ") if "=" in x]))
    x = [(x[0],x[1]),(x[2],x[3])]
    sensors.append(x)
    