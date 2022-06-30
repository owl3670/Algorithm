import unittest
from adjacency_list import Graph as GraphAL
from adjacency_matirix import Graph as GraphAM

class Tests(unittest.TestCase):
    # Test Adjacency_list
    def testAL(self):
        g1 = GraphAL()
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
        self.assertDictEqual(g1.graph, 
        {'A': [('B', 1), ('C', 1)], 
        'B': [('A', 1), ('C', 1), ('D', 1)], 
        'C': [('A', 1), ('B', 1)], 
        'D': [('B', 1)]})

    # Test Adjacency_matrix
    def testAM(self):
        g1 = GraphAM(5)
        g1.add_edge(0, 2)
        g1.add_edge(2, 0)
        g1.add_edge(0, 1)
        g1.add_edge(1, 0)
        g1.add_edge(1, 4)
        g1.add_edge(4, 1)
        g1.add_edge(2, 3)
        g1.add_edge(3, 2)
        self.assertListEqual(g1.graph, 
        [[0, 1, 1, 0, 0], 
        [1, 0, 0, 0, 1], 
        [1, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0], 
        [0, 1, 0, 0, 0]])

if __name__ == '__main__':
    unittest.main()