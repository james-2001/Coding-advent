from collections import deque

inpot = "364289715"
test = "389125467"
test2 = "328915467"

cups = deque(map(int,list(inpot)))
current_index = 0
n=100
for i in range(n):
    destination = (cups[current_index]-2)%9 +1
    current_cup = cups[0]
    cups.rotate(-1)
    pickup = [cups.popleft() for _ in range(3)]
    pickup.reverse()
    while destination in pickup:
        destination = (destination-2)%9 + 1
    destination_index = cups.index(destination)
    for c in pickup:
        cups.insert(destination_index+1, c)

while cups[-1]!= 1:
    cups.rotate()

output = ""
while cups[0]!=1:
    output+=str(cups.popleft())

print(output)