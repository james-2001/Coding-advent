f = open('test.txt', 'r')
ls = [line.replace('bags', 'bag').split('bag')
      for line in f.read().splitlines()]
ls = [list(filter(lambda s: len(s) != 1, line)) for line in ls]
ls = [list(map(lambda s: s.replace(' contain', '').strip(',. '), line))
      for line in ls]


bags = {line[0]: {bag[2:]: bag[0] for bag in line[1:]} for line in ls}


class Node:
    def __init__(self, colour, bags_dict) -> None:
        self.next: list = []
        self.prev: list = []
        self.colour: str = colour
        self.bags_dict: dict = bags_dict
    
    def find_prev(self):
        for key, value in self.bags_dict.items():
            if self.colour in value.keys():
                self.prev.append(key)


class Graph:
    def __init__(self) -> None:
        self.nodes: list = []


graph = Graph()

for colour, value in bags.items():
    colour_node = Node(colour, bags)
    colour_node.next = list(value.keys())
    colour_node.find_prev()
    graph.nodes.append(colour_node.colour)

for colour in graph.nodes:
    

