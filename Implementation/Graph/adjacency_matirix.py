from msilib.schema import Error


class Graph:
    def __init__(self, size) -> None:
        self.SIZE = size
        if size == 0:
            print('Size cannot be zero')
            raise ValueError
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

    def add_edge(self, origin, dest, weight=1) -> None:
        if origin < 0 or origin > self.SIZE or dest < 0 or dest > self.SIZE:
            print('Node number is invalid')
            return
        self.graph[origin][dest] = weight