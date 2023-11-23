class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        self.graph[vertex] = set()

    def add_edge(self, vertex1, vertex2):
        self.graph[vertex1].add(vertex2)
        self.graph[vertex2].add(vertex1)

    def color_graph(self):
        colors = {}  # Dictionary to store the color of each vertex

        for vertex in self.graph:
            # Initialize the set of unavailable colors for the current vertex
            unavailable_colors = set(colors.get(neighbor, None) for neighbor in self.graph[vertex])

            # Find the first available color
            for color in range(len(self.graph)):
                if color not in unavailable_colors:
                    colors[vertex] = color
                    break

        return colors

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    vertices = ['A', 'B', 'C', 'D', 'E']
    for vertex in vertices:
        g.add_vertex(vertex)

    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('C', 'E'), ('D', 'E')]
    for edge in edges:
        g.add_edge(edge[0], edge[1])

    # Color the graph
    coloring = g.color_graph()

    # Output the result
    for vertex, color in coloring.items():
        print(f"Vertex {vertex} is colored with color {color}")
