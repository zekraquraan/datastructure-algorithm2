class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Graph:
    def __init__(self):
        self.nodes = []

    def depth_first(self, start_node):
        if not self.nodes:
            return []
        
        visited = set()
        result = []
        self._depth_first_recursive(start_node, visited, result)
        return result

    def _depth_first_recursive(self, node, visited, result):
        if node not in visited:
            visited.add(node)
            result.append(node.value)
            for neighbor in node.neighbors:
                self._depth_first_recursive(neighbor, visited, result)

        

# Create nodes
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

# Create graph and add nodes/edges
graph = Graph()
graph.nodes = [A, B, C, D, E, F, G, H]
A.neighbors = [B, C, G]
B.neighbors = [D, E]
C.neighbors = [F]
E.neighbors = [H]

# Test the depth_first method
result = graph.depth_first(A)
print(', '.join(result))  # Output: A, B, D, E, H, C, F, G
