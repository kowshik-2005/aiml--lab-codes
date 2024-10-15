def depth_limited_dfs(graph, node, depth, visited):
    if depth == 0 and node not in visited:
        print(node, end=" ")
        visited.add(node)
        return True
    elif depth > 0:
        for neighbor in graph[node]:
            if neighbor not in visited:
                if depth_limited_dfs(graph, neighbor, depth - 1, visited):
                    return True
    return False

def iddfs(graph, start, max_depth):
    for depth in range(max_depth):
        print(f"\nDepth: {depth}")
        visited = set()
        depth_limited_dfs(graph, start, depth, visited)

print("IDDFS traversal starting from vertex A up to depth 3:")
iddfs(graph, 'A', 3)
