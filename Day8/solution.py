f = open('input.txt', 'r')
ls = [line.split() for line in f.read().splitlines()]


class Boot:
    def __init__(self, code) -> None:
        self.pos: int = 0
        self.accumulator: int = 0
        self.code: list = code
        self.code.append(['fin', '0'])
        self.pos_history: list = []
        self.booted: bool = False

    def reset(self):
        self.accumulator = 0
        self.pos = 0
        self.pos_history = []

    def switch(self, index):
        cmd = self.code[int(index)][0]
        self.code[index][0] = 'jmp' if cmd == 'nop' else 'nop'

    def jmp(self, n):
        self.pos_history.append(self.pos)
        self.pos += n

    def acc(self, n):
        self.accumulator += n
        self.jmp(1)

    def nop(self, n):
        self.jmp(1)

    def fin(self, n):
        self.booted = True

    def start(self):
        while self.pos not in self.pos_history and not self.booted:
            instruction, value = self.code[self.pos]
            value = int(value)
            eval(f'self.{instruction}({value})')

    def corrupted_start(self):
        for i in range(len(self.code)):
            self.reset()
            if self.code[i][0] in ['jmp', 'nop']:
                self.switch(i)
                self.start()
                self.switch(i)
            else:
                self.start()
            if self.booted:
                return self.accumulator


boot = Boot(ls)
boot.start()
print(f'Part 1: {boot.accumulator}')
boot.reset()
print(f'part 2: {boot.corrupted_start()}')
