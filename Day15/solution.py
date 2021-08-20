def play(n):
    spoken = [8, 13, 1, 0, 18, 9]
    prev = spoken[-1]
    history = {number: turn + 1 for turn, number in enumerate(spoken)}
    for i in range(6, n):
        history[prev], prev = i, i - history[prev] if prev in history else 0
    return prev


print(f'Part 1: {play(2020)}')
print(f'Part 2: {play(30000000)}')
