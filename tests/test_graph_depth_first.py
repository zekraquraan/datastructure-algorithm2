import unittest
from graph_depth_first.graph_depth_first import Node, Graph

class TestGraphMethods(unittest.TestCase):
    def setUp(self):
        # Create nodes
        self.A = Node('A')
        self.B = Node('B')
        self.C = Node('C')
        self.D = Node('D')
        self.E = Node('E')
        self.F = Node('F')
        self.G = Node('G')
        self.H = Node('H')

        # Create graph and add nodes/edges
        self.graph = Graph()
        self.graph.nodes = [self.A, self.B, self.C, self.D, self.E, self.F, self.G, self.H]
        self.A.neighbors = [self.B, self.C, self.G]
        self.B.neighbors = [self.D, self.E]
        self.C.neighbors = [self.F]
        self.E.neighbors = [self.H]

    def test_depth_first(self):
        result = self.graph.depth_first(self.A)
        expected_result = ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
        self.assertEqual(result, expected_result)

    def test_depth_first_with_single_node(self):
        single_node_graph = Graph()
        node = Node('X')
        single_node_graph.nodes = [node]
        result = single_node_graph.depth_first(node)
        self.assertEqual(result, ['X'])

    def test_depth_first_with_disconnected_nodes(self):
        I = Node('I')
        J = Node('J')
        K = Node('K')
        L = Node('L')
        self.graph.nodes.extend([I, J, K, L])
        result = self.graph.depth_first(self.A)
        expected_result = ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
        self.assertEqual(result, expected_result)

    def test_depth_first_on_empty_graph(self):
        empty_graph = Graph()
        result = empty_graph.depth_first(self.A)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()
