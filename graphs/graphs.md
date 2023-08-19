# Graphs



## Approach & Efficiency
Time Complexity:

add_vertex: This method has a time complexity of O(1) because it involves inserting a value into a dictionary, which has constant time complexity.
add_edge: Similarly, this method has a time complexity of O(1) for the same reason.
get_vertices: Constructing a list of keys from a dictionary takes O(n) time where n is the number of vertices in the graph.
get_neighbors: This method retrieves neighbors from the adjacency list, which has a time complexity of O(1) for each vertex. However, when called for all vertices, the overall time complexity becomes O(V + E), where V is the number of vertices and E is the number of edges.
size: The len function used here takes O(1) time complexity since the length of the dictionary is maintained internally.
Overall, the time complexity of the provided code depends on the number of vertices (V) and edges (E) in the graph.

Space Complexity:

The space complexity of the Graph class is O(V + E), where V is the number of vertices and E is the number of edges. This is due to the storage of vertices in a dictionary and their corresponding neighbors in lists.
The get_vertices method creates a list of vertices, contributing O(V) space complexity.
The get_neighbors method returns a list of neighbors for a vertex, which can take up O(E) space in the worst case.
## Solution
 python graphs.py