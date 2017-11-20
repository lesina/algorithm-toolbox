#Uses python3

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


# def bfs(matrix, start, end):
#     queue = [start]
#     visited = [False]*len(matrix)
#     answer = 0
#     # alarm = 1
#     # midQueue = []
#     while queue:
#         current = queue.pop(0)
#         # alarm -= 1
#         visited[current] = True
#         for vertex in range(len(matrix)):
#             if vertex != end and matrix[current][vertex] != float('inf') \
#                     and not visited[vertex] and vertex not in queue:
#                 queue.append(vertex)
#                 matrix[start][vertex] = min(matrix[start][vertex], matrix[current][vertex]+1)
#                 # alarm += 1
#             elif vertex == end and matrix[current][vertex] != float('inf'):
#                 matrix[start][vertex] = min(matrix[start][vertex], matrix[current][vertex] + 1)
#                 return matrix
#     return matrix


def bfs(matrix, start):
    dist = [None] * (vertexes)
    dist[start] = 0
    queue = [start]
    Qstart = 0
    while Qstart < len(queue):
        u = queue[Qstart]
        Qstart += 1
        # adj = [ i for i in range(vertexes) if matrix[u][i]]
        for v in matrix[u]:
            if dist[v] is None:
                dist[v] = dist[u] + 1
                queue.append(v)
    return dist


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
start, end = list(map(int, input().split()))
start -= 1
end -= 1
answer = bfs(matrix, start) #, end)[start][end]
# A = [[matrix[i][j] for j in range(vertexes)] for i in range(vertexes)]
# for k in range(vertexes):
#     for i in range(vertexes):
#
#         for j in range(vertexes):
#             matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
# answer = matrix[start][end]
# if answer == float('inf'):
#     print(-1)
# else:
#     print(answer)
if answer[end] is None:
    print(-1)
else:
    print(answer[end])