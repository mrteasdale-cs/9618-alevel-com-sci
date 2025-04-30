def create_graph():
    return {}

def add_vertex(graph, vertex):
    if vertex not in graph:
        graph[vertex] = []

def add_edge(graph, vertex1, vertex2):
    if vertex1 not in graph:
        add_vertex(graph, vertex1)
    if vertex2 not in graph:
        add_vertex(graph, vertex2)
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)

def display_graph(graph):
    for vertex, edges in graph.items():
        print(f"{vertex}: {', '.join(map(str, edges))}")

# Example usage
graph = create_graph()
# Adding vertices
add_vertex(graph, 'A')
add_vertex(graph, 'B')
add_vertex(graph, 'C')
add_vertex(graph, 'D')
# Adding edges
add_edge(graph, 'A', 'B')
add_edge(graph, 'A', 'C')
add_edge(graph, 'B', 'C')
add_edge(graph, 'C', 'D')
# Display the graph
display_graph(graph)
