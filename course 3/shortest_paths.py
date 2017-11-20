#Uses python3

def make_adjacency_matrix(vertexes, edges):
    matrix = dict()
    for i in range(vertexes):
        matrix[i] = dict()
    for i in range(edges):
        vertex1, vertex2, weight = list(map(int, input().split()))
        vertex1 -= 1
        vertex2 -= 1
        matrix[vertex1][vertex2] = weight
        # matrix[vertex2].append(vertex1)
    return matrix

def initialize(graph, source):
    d = {}
    p = {}
    for node in graph:
        d[node] = float('Inf')
        p[node] = None
    d[source] = 0
    return d, p

def relax(node, neighbour, graph, d, p):
    if d[neighbour] > d[node] + graph[node][neighbour]:
        d[neighbour]  = d[node] + graph[node][neighbour]
        p[neighbour] = node

def bellman_ford(graph, source):
    d, p = initialize(graph, source)
    decision = {i : 'ok' for i in range(vertexes)}
    for i in range(vertexes - 1):
        for u in graph:
            for v in graph[u]:
                relax(u, v, graph, d, p)
    for i in range(2):
        for u in graph:
            for v in graph[u]:
                # print(v, d[v])
                # print(u, d[u], graph[u][v])
                # assert d[v] <= d[u] + graph[u][v]
                if d[v] > d[u] + graph[u][v]:
                    decision[v] = 'not ok'
                    d[v] = -float('inf')
                    # d[v] = d[u] + graph[u][v]
                #     d[v] = -float('inf')
                #     d[u] = -float('inf')
    return d, decision

vertexes, edges = list(map(int, input().split()))
matrix = make_adjacency_matrix(vertexes, edges)
start = int(input())
start -= 1
# print(matrix)
answer, correct = bellman_ford(matrix, start)
for i in range(vertexes):
    if correct[i] == 'ok' and answer[i] != float('inf'):
        print(answer[i])
    elif correct[i] == 'ok':
        print('*')
    else:
        print('-')