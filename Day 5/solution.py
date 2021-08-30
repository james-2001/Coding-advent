f = open('input.txt', 'r')
ls = [line[:-1] for line in f.readlines()]

seat_id = [int(seat.replace('F', '0').replace('B', '1')
           .replace('L', '0').replace('R', '1'), 2) for seat in ls]

print(f'Part 1: {max(seat_id)}')

for seat in seat_id:
    if seat+1 not in seat_id and seat + 2 in seat_id:
        print(f'part 2: {seat+1}')
