class Graph:
    def __init__(self) -> None:
        self.size = 0
        self.graph = {}
    
    def add_node(self, node) -> None:
        if node in self.graph:
            print('Node already exists')
            return
        self.graph[node] = []
    
    def add_edge(self, start, end) -> None:
        if start not in self.graph or end not in self.graph:
            print('Node does not exists')
            return
        for node in self.graph[start]:
            if end in node:
                print('Edge already exists')
                return
        self.graph[start].append((end, 1))
        self.size += 1
    
    def add_weighted_edge(self, start, end, weight) -> None:
        if start not in self.graph or end not in self.graph:
            print('Node does not exists')
        for node in self.graph[start]:
            if end in node: 
                print('Edge already exists')
                return
        self.graph[start].append((end, weight))
        self.size += 1
    
g1 = Graph()
g1.add_node('A')
g1.add_node('B')
g1.add_node('C')
g1.add_node('D')
g1.add_edge('A', 'B')
g1.add_edge('B', 'A')
g1.add_edge('A', 'C')
g1.add_edge('C', 'A')
g1.add_edge('B', 'C')
g1.add_edge('C', 'B')
g1.add_edge('B', 'D')
g1.add_edge('D', 'B')
print(g1.graph)