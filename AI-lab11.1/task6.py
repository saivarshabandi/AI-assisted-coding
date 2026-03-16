# Write Python code to implement a Graph using an adjacency list representation.
# Include methods add_vertex(), add_edge(), and display_graph().
# Add comments and docstrings explaining each method.
# Also include an example showing how vertices and edges are added.
class Graph:
    """
    A Graph data structure implementation using an adjacency list representation.
    The graph can be directed or undirected based on the add_edge method.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Parameters:
        vertex: The vertex to be added to the graph.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2, directed=False):
        """
        Add an edge between two vertices in the graph.

        Parameters:
        vertex1: The first vertex of the edge.
        vertex2: The second vertex of the edge.
        directed: If True, the edge is directed from vertex1 to vertex2. 
                  If False, the edge is undirected (default is False).
        """
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        if not directed:
            self.graph[vertex2].append(vertex1)

    def display_graph(self):
        """Display the adjacency list representation of the graph."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {edges}")

# Example usage of the Graph class
if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")

    graph.add_edge("A", "B")
    graph.add_edge("B", "C")

    print("Graph representation:")
    graph.display_graph()