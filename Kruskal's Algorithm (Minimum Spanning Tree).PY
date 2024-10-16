def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    if root_x != root_y:
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        elif rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

def kruskal(graph, vertices):
    mst = []
    parent = []
    rank = []
    graph = sorted(graph, key=lambda item: item[2])

    for node in range(vertices):
        parent.append(node)
        rank.append(0)

    for edge in graph:
        u, v, w = edge
        root_u = find(parent, u)
        root_v = find(parent, v)
        if root_u != root_v:
            mst.append(edge)
            union(parent, rank, root_u, root_v)

    return mst

graph = [
    [0, 1, 10], [0, 2, 6], [0, 3, 5],
    [1, 3, 15], [2, 3, 4]
]
vertices = 4
mst = kruskal(graph, vertices)
print("Minimum Spanning Tree:", mst)
