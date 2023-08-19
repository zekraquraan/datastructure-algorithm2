class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices[value] = []
        return value

    def add_edge(self, vertex1, vertex2, weight=None):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append((vertex2, weight))
            self.vertices[vertex2].append((vertex1, weight))
    
    def get_vertices(self):
        return list(self.vertices.keys())
    
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        return []
    
    def size(self):
        return len(self.vertices)
if __name__=="__main__":
    graph = Graph()

    # Add vertices
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    # Add edges
    graph.add_edge("A", "B", 5)
    graph.add_edge("B", "C", 3)
    graph.add_edge("C", "A", 2)

    # Get vertices and print
    print("Vertices:", graph.get_vertices())

    # Get neighbors and print
    print("Neighbors of A:", graph.get_neighbors("A"))
    print("Neighbors of B:", graph.get_neighbors("B"))
    print("Neighbors of C:", graph.get_neighbors("C"))

    # Get size and print
    print("Size:", graph.size())
  