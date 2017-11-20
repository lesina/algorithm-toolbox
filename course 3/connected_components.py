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
        matrix[vertex2][vertex1] = 1
    return matrix


def bfs(matrix, start):
    queue = [start]
    visited = [False]*len(matrix)
    answer = 1
    while False in visited:
        if queue:
            current = queue.pop(0)
        else:
            current = visited.index(False)
            answer += 1
        visited[current] = True
        for vertex in range(len(matrix)):
            if matrix[current][vertex] and not visited[vertex]:
                queue.append(vertex)
    return answer


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
print(bfs(matrix, 0))