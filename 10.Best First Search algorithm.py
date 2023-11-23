from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))

    while not priority_queue.empty():
        current_cost, current_node = priority_queue.get()

        if current_node == goal:
            print("Goal reached:", current_node)
            return True

        if current_node not in visited:
            print("Visiting:", current_node)
            visited.add(current_node)

            for neighbor, cost in graph.graph[current_node]:
                if neighbor not in visited:
                    priority_queue.put((cost, neighbor))

    print("Goal not reached.")
    return False

# Example usage
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_edge('A', [('B', 4), ('C', 5)])
    g.add_edge('B', [('D', 7)])
    g.add_edge('C', [('D', 2)])
    g.add_edge('D', [])

    # Perform Best-First Search from 'A' to 'D'
    start_node = 'A'
    goal_node = 'D'
    best_first_search(g, start_node, goal_node)
