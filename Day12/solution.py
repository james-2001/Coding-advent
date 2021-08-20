f = open('input.txt', 'r')
ls = [line for line in f.read().splitlines()]


class Navigate:
    def __init__(self, instructions, waypoint) -> None:
        self.position = 0+0j
        self.instructions = instructions
        self.distance = 0
        self.waypoint = waypoint[0] + (1j)*waypoint[1]

    def nav(self):
        for line in self.instructions:
            eval(f'self.{line[0]}({line[1:]})')

    def man_distance(self):
        self.distance = int(abs(self.position.real)+abs(self.position.imag))

    def F(self, n):
        self.position += n*self.waypoint

    def R(self, n):
        self.waypoint *= (0+1j) ** (n//90)

    def L(self, n):
        self.waypoint *= (0-1j) ** (n//90)


class Part1(Navigate):
    def __init__(self, instructions, waypoint) -> None:
        super().__init__(instructions, waypoint)

    def N(self, n):
        self.position += n+0j

    def E(self, n):
        self.position += (0+1j)*n

    def S(self, n):
        self.position += -n + 0j

    def W(self, n):
        self.position += (0-1j)*n


class Part2(Navigate):
    def __init__(self, instructions, waypoint) -> None:
        super().__init__(instructions, waypoint)

    def N(self, n):
        self.waypoint += n+0j

    def E(self, n):
        self.waypoint += (0+1j)*n

    def S(self, n):
        self.waypoint += -n + 0j

    def W(self, n):
        self.waypoint += (0-1j)*n


for part, wp in {1: (0, 1), 2: (1, 10)}.items():
    n = eval(f'Part{part}(ls, {wp})')
    n.nav()
    n.man_distance()
    print(f'Part {part}: {n.distance}')
