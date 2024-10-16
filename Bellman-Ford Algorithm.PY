def bellman_ford(graph, start, vertices):
    distance = {vertex: float('infinity') for vertex in vertices}
    distance[start] = 0

    for _ in range(len(vertices) - 1):
        for u, v, w in graph:
            if distance[u] + w < distance[v]:
                distance[v] = distance[u] + w

    for u, v, w in graph:
        if distance[u] + w < distance[v]:
            print("Graph contains negative weight cycle")
            return None

    return distance

edges = [
    ('A', 'B', -1), ('A', 'C', 4),
    ('B', 'C', 3), ('B', 'D', 2), ('B', 'E', 2),
    ('D', 'B', 1), ('D', 'C', 5), ('E', 'D', -3)
]
vertices = ['A', 'B', 'C', 'D', 'E']
print(bellman_ford(edges, 'A', vertices))
