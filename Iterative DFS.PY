# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

# Iterative DFS function
def iterative_dfs(graph, start):
    visited = set()  # Set for visited nodes
    stack = [start]  # Initialize a stack with the starting node

    while stack:
        vertex = stack.pop()  # Pop a vertex from the stack
        if vertex not in visited:
            print(vertex, end=" ")  # Output the current vertex
            visited.add(vertex)  # Mark it as visited

            # Add unvisited neighbors to the stack
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)

# Call Iterative DFS starting from vertex 'A'
print("Iterative DFS traversal starting from vertex A:")
iterative_dfs(graph, 'A')
