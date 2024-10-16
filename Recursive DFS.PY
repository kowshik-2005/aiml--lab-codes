# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Recursive DFS function
def dfs(graph, vertex, visited=None):
    if visited is None:
        visited = set()  # Initialize visited set if it's the first call
    visited.add(vertex)
    print(vertex, end=" ")  # Output the current vertex

    # Recur for all the neighbors of this vertex
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Call DFS starting from vertex 'A'
print("DFS traversal starting from vertex A:")
dfs(graph, 'A')
