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


def bfs(matrix, start, end):
    queue = [start]
    visited = [False]*len(matrix)
    answer = 0
    while queue:
        current = queue.pop(0)
        visited[current] = True
        for vertex in range(len(matrix)):
            if vertex != end and matrix[current][vertex] and not visited[vertex]:
                queue.append(vertex)
            elif vertex == end and matrix[current][vertex]:
                answer = 1
    return answer


vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
start, end = list(map(int, input().split()))
start -= 1
end -= 1
print(bfs(matrix, start, end))