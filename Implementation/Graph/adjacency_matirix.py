class Graph:
    def __init__(self, size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, origin, dest) -> None:
        self.graph[origin][dest] = 1
    
    def add_weighted_edge(self, origin, dest, weight) -> None:
        self.graph[origin][dest] = weight

g1 = Graph(5)
g1.add_edge(0, 2)
g1.add_edge(2, 0)
g1.add_edge(0, 1)
g1.add_edge(1, 0)
g1.add_edge(1, 4)
g1.add_edge(4, 1)
g1.add_edge(2, 3)
g1.add_edge(3, 2)

print(g1.graph)