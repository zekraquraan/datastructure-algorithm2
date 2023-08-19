import unittest
from graphs.graphs import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_add_vertex(self):
        self.graph.add_vertex("A")
        self.assertIn("A", self.graph.get_vertices())

    def test_add_edge(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_edge("A", "B", 5)
        neighbors_of_a = self.graph.get_neighbors("A")
        neighbors_of_b = self.graph.get_neighbors("B")
        self.assertEqual(len(neighbors_of_a), 1)
        self.assertEqual(neighbors_of_a[0][0], "B")
        self.assertEqual(neighbors_of_a[0][1], 5)
        self.assertEqual(len(neighbors_of_b), 1)
        self.assertEqual(neighbors_of_b[0][0], "A")
        self.assertEqual(neighbors_of_b[0][1], 5)

    def test_get_vertices(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        vertices = self.graph.get_vertices()
        self.assertIn("A", vertices)
        self.assertIn("B", vertices)

    def test_get_neighbors(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.graph.add_edge("A", "B", 5)
        self.graph.add_edge("B", "C", 3)
        neighbors_of_b = self.graph.get_neighbors("B")
        self.assertEqual(len(neighbors_of_b), 2)
        self.assertIn(("A", 5), neighbors_of_b)
        self.assertIn(("C", 3), neighbors_of_b)

    def test_size(self):
        self.graph.add_vertex("A")
        self.graph.add_vertex("B")
        self.graph.add_vertex("C")
        self.assertEqual(self.graph.size(), 3)

if __name__ == '__main__':
    unittest.main()