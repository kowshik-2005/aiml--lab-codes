def is_safe(graph, color, node, c):
    for neighbor in graph[node]:
        if color[neighbor] == c:
            return False
    return True

def graph_coloring(graph, color, node, max_colors):
    if node == len(graph):
        return True
    
    for c in range(1, max_colors + 1):
        if is_safe(graph, color, node, c):
            color[node] = c
            if graph_coloring(graph, color, node + 1, max_colors):
                return True
            color[node] = 0
    return False

graph = [[1, 2], [0, 2], [0, 1, 3], [2]]
max_colors = 3
color = [0] * len(graph)

if graph_coloring(graph, color, 0, max_colors):
    print(f"Colors assigned: {color}")
else:
    print("No solution")
