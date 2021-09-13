from collections import deque

inpot = "364289715"
test = "389125467"
test2 = "328915467"

cups = deque(map(int,list(inpot)))
cups.rotate(-1)
current_index = 0

def rotate_past(deq: deque, element):
    while deq[-1]!= element:
        deq.rotate(-1)


def simulate(cups: deque,n):
    for _ in range(n):
        current = cups[-1]
        destination = (current-2)%9 +1
        pickup = [cups.popleft() for _ in range(3)]
        pickup.reverse()
        while destination in pickup:
            destination = (destination-2)%9 + 1
        rotate_past(cups, destination) 
        cups.extendleft(pickup)
        rotate_past(cups, current)
        cups.rotate(-1)
    return cups


def pt1_output(cups):
    while cups[-1]!= 1:
        cups.rotate()
    output = ""
    while cups[0]!=1:
        output+=str(cups.popleft())
    return output

def pt2_output(cups):
    for i in range(0,len(cups)):
        if cups[i] == 1:
            return([cups[i+1], cups[i+2]])

print(pt1_output(simulate(cups,100)))
# cups = deque(map(int,list(inpot))) + deque(range(10, 10000000))
# x= simulate(cups, 10000000)
# print("nearly there")
# print(pt2_output(x))



