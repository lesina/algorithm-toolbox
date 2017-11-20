#Uses python3

import sys
sys.setrecursionlimit(100000)

n, m = list(map(int, input().split()))
adj = [[] for i in range(n)]
adjT = [[] for i in range(n)]
graph = [[] for i in range(n)]
used = [False for i in range(n)]
color = [int(0) for i in range(n)]
topSort = []
component = [int(0) for i in range(n)]

def read_graph_as_lists(N,M):
    graph = [[] for i in range(N)]
    for edge in range(M):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    return graph

for i in range(m):
    v, w = map(int, input().split())
    v -= 1
    w -= 1
    graph[v].append(w)
    graph[w].append(v)
    adj[v].append(w)
    adjT[w].append(v)

def dfs_1(vertex, graph, used = set()):
    used.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour not in used:
            dfs_1(neighbour, graph, used)

def dfs(v):
    if used[v]:
        return
    used[v] = True
    for w in adj[v]:
        dfs(w)
    topSort.append(v)

def ccs(v, componentID):
    if used[v]:
        return
    used[v] = True
    component[v] = componentID
    for w in adjT[v]:
        ccs(w, componentID)

def run():
    for v in range(n):
        dfs(v)
    for i in range(n):
        used[i] = False
    componentID = 0
    for v in reversed(topSort):
        if not used[v]:
            ccs(v, componentID)
            componentID = componentID + 1

    isp = set()
    number_of_components = 0
    for vertex in range(len(graph)):
        if vertex not in isp:
            dfs_1(vertex, graph, isp)
            number_of_components += 1
    print(componentID)

run()