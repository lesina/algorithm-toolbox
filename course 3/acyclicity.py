#Uses python3

def make_adjacency_matrix(vertexes, edges):
    matrix = list()
    for i in range(vertexes):
        matrix.append([0]*vertexes)
    for i in range(edges):
        vertex1, vertex2 = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        matrix[vertex1][vertex2] = 1
    return matrix


def bfs(matrix, start):
    queue = [start]
    visited = [False]*len(matrix)
    answer = 0
    while queue:
        current = queue.pop(0)
        visited[current] = True
        for vertex in range(len(matrix)):
            if matrix[current][vertex] and not visited[vertex]:
                queue.append(vertex)
            elif matrix[current][vertex] and vertex == start:
                answer = 1
        if answer:
            break
    return answer


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
answer = 0
i = 0
while not answer and i < vertexes:
    answer = bfs(matrix, i)
    i += 1
print(answer)