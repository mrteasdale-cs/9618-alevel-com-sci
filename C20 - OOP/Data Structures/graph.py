class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
            self.graph[vertex1].append(vertex2)

    def display(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join(self.graph[vertex])}")
            # Example usage
            g = Graph()
            g.add_edge("A", "B")
            g.add_edge("A", "C")
            g.add_edge("B", "D")
            g.display()

