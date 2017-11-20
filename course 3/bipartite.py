#Uses python3

# def make_adjacency_matrix(vertexes, edges):
#     matrix = list()
#     for i in range(vertexes):
#         matrix.append([0]*vertexes)
#     for i in range(edges):
#         vertex1, vertex2 = list(map(int, input().split()))
#         vertex1 -= 1
#         vertex2 -= 1
#         matrix[vertex1][vertex2] = 1
#         matrix[vertex2][vertex1] = 1
#     return matrix


def make_adjacency_matrix(vertexes, edges):
    matrix = dict()
    for i in range(vertexes):
        matrix[i] = []
    for i in range(edges):
        vertex1, vertex2 = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        matrix[vertex1].append(vertex2)
        matrix[vertex2].append(vertex1)
    return matrix


def bfs(matrix, start):
    dist = [None] * (vertexes)
    dist[start] = 0
    queue = [start]
    Qstart = 0
    while Qstart < len(queue):
        u = queue[Qstart]
        Qstart += 1
        for v in matrix[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


# def bipartite(matrix, start):
#     colors = [-1]*vertexes
#     colors[start] = 1
#     queue = [start]
#     while queue:
#         u = queue.pop(0)
#         for v in range(vertexes):
#             if matrix[u][v] and colors[v]==-1:
#                 colors[v] = 1 - colors[u]
#                 queue.append(v)
#             elif matrix[u][v] and colors[u]==colors[v]:
#                 return False
#     return True


def bipartite(matrix, start):
    colors = [-1]*vertexes
    colors[start] = 1
    queue = [start]
    while queue:
        u = queue.pop(0)
        for v in matrix[u]:
            if colors[v]==-1:
                colors[v] = 1 - colors[u]
                queue.append(v)
            elif colors[u]==colors[v]:
                return False
    return True


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
if bipartite(matrix, 0):
    print(1)
else:
    print(0)