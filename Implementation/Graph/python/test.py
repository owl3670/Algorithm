import unittest
from adjacency_list import Graph as GraphAL
from adjacency_matirix import Graph as GraphAM
from dfs import dfsAL, dfsAM
from bfs import bfsAL, bfsAM


class Tests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.g1 = GraphAL()
        self.g1.add_node('A')
        self.g1.add_node('B')
        self.g1.add_node('C')
        self.g1.add_node('D')
        self.g1.add_edge('A', 'B')
        self.g1.add_edge('B', 'A')
        self.g1.add_edge('A', 'C')
        self.g1.add_edge('C', 'A')
        self.g1.add_edge('B', 'C')
        self.g1.add_edge('C', 'B')
        self.g1.add_edge('B', 'D')
        self.g1.add_edge('D', 'B')

        self.g2 = GraphAM(6)
        self.g2.add_edge(0, 2)
        self.g2.add_edge(2, 0)
        self.g2.add_edge(0, 1)
        self.g2.add_edge(1, 0)
        self.g2.add_edge(1, 4)
        self.g2.add_edge(4, 1)
        self.g2.add_edge(2, 3)
        self.g2.add_edge(3, 2)
        self.g2.add_edge(4, 5)
        self.g2.add_edge(5, 4)

    # Test Adjacency_list

    def testAL(self):
        self.assertDictEqual(self.g1.graph,
                             {'A': [('B', 1), ('C', 1)],
                              'B': [('A', 1), ('C', 1), ('D', 1)],
                              'C': [('A', 1), ('B', 1)],
                              'D': [('B', 1)]})

    # Test Adjacency_matrix
    def testAM(self):
        self.assertListEqual(self.g2.graph,
                             [[0, 1, 1, 0, 0, 0],
                              [1, 0, 0, 0, 1, 0],
                              [1, 0, 0, 1, 0, 0],
                              [0, 0, 1, 0, 0, 0],
                              [0, 1, 0, 0, 0, 1],
                              [0, 0, 0, 0, 1, 0]])

    # Test DFS
    def testDFS(self):
        self.assertListEqual(dfsAL(self.g1.graph, 'A'),
                             ['A', 'C', 'B', 'D'])
        self.assertListEqual(dfsAM(self.g2.graph, 0),
                             [0, 2, 3, 1, 4, 5])

    # Test BFS
    def testBFS(self):
        self.assertListEqual(bfsAL(self.g1.graph, 'A'),
                             ['A', 'B', 'C', 'D'])
        self.assertListEqual(bfsAM(self.g2.graph, 0),
                             [0, 1, 2, 4, 3, 5])

if __name__ == '__main__':
    unittest.main()
