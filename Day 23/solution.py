from collections import deque

inpot = "364289715"
test = "389125467"
test2 = "328915467"

cups = deque(map(int,list(test)))
current_index = 0
n=10
for i in range(n):
    destination = cups[current_index]-1
    #print(destination, current_index)
    x = cups[current_index]
    cups.rotate(-(current_index+1))
    pickup = [cups.popleft() for _ in range (3)]
    while destination in pickup:
        destination = ((destination -2)%len(cups)) +1
    print(destination,x)
    pickup.reverse()
    while destination != cups[0]:
        cups.rotate(-1)
    cups.extendleft(pickup)
    current_index = (current_index + 1) % len(cups) 

print(cups)
