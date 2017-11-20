# Uses python3

def make_adjacency_matrix(vertexes, edges):
    matrix = list()
    for i in range(vertexes):
        matrix.append([100000] * vertexes)
    for i in range(edges):
        vertex1, vertex2, weight = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        matrix[vertex1][vertex2] = weight
        # matrix[vertex2][vertex1] = weight
    return matrix


# def bfs(matrix, start, end):
#     queue = [start]
#     visited = [False]*len(matrix)
#     distance = [float('inf')]*len(matrix)
#     distance[start] = 0
#     # answer = 0
#     current = queue.pop(0)
#     while queue:
#         visited[current] = True
#         min_id = current
#         MIN = float('inf')
#         for vertex in range(len(matrix)):
#             if matrix[current][vertex] and not visited[vertex]:
#                 queue.append(vertex)
#             if matrix[current][vertex] and distance[current]+1 < distance[vertex]:
#                 distance[vertex] = distance[current]+1
#                 if distance[vertex] < MIN:
#                     MIN = distance[vertex]
#                     min_id = vertex
#
#         current = min_id


def Dexter(size, start, adjacency_matrix):
    valid = [True] * size
    weight = [100000] * size
    weight[start] = 0
    for i in range(size):
        min_weight = 100001
        ID_min_weight = -1
        for i in range(size):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                ID_min_weight = i
        for i in range(size):
            if weight[ID_min_weight] + adjacency_matrix[ID_min_weight][i] <= weight[i]:
                weight[i] = weight[ID_min_weight] + adjacency_matrix[ID_min_weight][i]
        valid[ID_min_weight] = False
    return weight


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
start, end = list(map(int, input().split()))
start -= 1
end -= 1
answer = Dexter(vertexes, start, matrix)[end]
if answer == 100000:
    print(-1)
else:
    print(answer)
