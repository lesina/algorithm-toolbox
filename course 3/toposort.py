#Uses python3
from collections import deque
# def make_adjacency_matrix(vertexes, edges):
#     matrix = list()
#     for i in range(vertexes):
#         matrix.append([0]*vertexes)
#     for i in range(edges):
#         vertex1, vertex2 = list(map(int, input().split()))
#         vertex1 -= 1
#         vertex2 -= 1
#         matrix[vertex1][vertex2] = 1
#     return matrix


def make_matrix(vertexes, edges):
    matrix = [ [i, []] for i in range(vertexes) ]
    for i in range(edges):
        vertex1, vertex2 = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        matrix[vertex1][1].append(vertex2)
    return dict(matrix)


# def bfs(matrix, start):
#     queue = [start]
#     visited = [False]*len(matrix)
#     answer = 0
#     while queue:
#         current = queue.pop(0)
#         visited[current] = True
#         for vertex in range(len(matrix)):
#             if matrix[current][vertex] and not visited[vertex]:
#                 queue.append(vertex)
#             elif matrix[current][vertex] and vertex == start:
#                 answer = 1
#         if answer:
#             break
#     return answer


def topological_sort(graph):
    GRAY, BLACK = 0, 1
    order, enter, state = deque(), set(graph), {}

    def dfs(node):
        state[node] = GRAY
        for k in graph.get(node, ()):
            sk = state.get(k, None)
            if sk == GRAY: raise ValueError("cycle")
            if sk == BLACK: continue
            enter.discard(k)
            dfs(k)
        order.appendleft(node)
        state[node] = BLACK

    while enter:
        dfs(enter.pop())
    return order


vertexes, edges = list(map(int, input().split()))
matrix = make_matrix(vertexes, edges)
answer = 0
i = 0
# while not answer and i < vertexes:
#     answer = bfs(matrix, i)
#     i += 1
# print(answer)
order = [i+1 for i in topological_sort(matrix)]
print(*order)