class Graph:
    def __init__(self) -> None:
        self.size = 0
        self.graph = {}

    def add_node(self, node) -> None:
        if node in self.graph:
            print('Node already exists')
            return
        self.graph[node] = []
        self.size += 1

    def add_edge(self, start, end, weight=1) -> None:
        if start not in self.graph or end not in self.graph:
            print('Node does not exists')
            return
        for node in self.graph[start]:
            if end in node:
                print('Edge already exists')
                return
        self.graph[start].append((end, weight))
