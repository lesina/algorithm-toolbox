#Uses python3
def BellmanFord():
    for j in range(n-1):
        for u in graph:
            for v, weight in graph[u]:
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight
                    global change
                    change = True
                if distance[u] == infinity and distance[v] != infinity:
                    distance[u] = distance[v] - weight


n, m = list(map(int, input().split()))
if n == 0 or m == 0:
    print(0)
    exit()
graph = {}
seen = {}
infinity = float("inf")
visited = [False] * (n + 1)
distance = [infinity] * (n + 1)
dist = infinity
for i in range(1, n+1):
    graph[i] = set()
for i in range(m):
    u, v, w = map(int, input().split())
    if u == v and w >= 0:
        continue
    if u not in graph:
        graph[u].add((v, w))
        seen[(u, v)] = w
    else:
        if (u, v) in seen:
            if w < seen[(u, v)]:
                graph[u].remove((v, seen[(u, v)]))
                graph[u].add((v, w))
                seen[(u, v)] = w
        else:
            graph[u].add((v, w))
            seen[(u, v)] = w
distance[u] = 0
BellmanFord()
change = False
result = 0
for u in graph:
    for v, weight in graph[u]:
        if distance[u] + weight < distance[v]:
            distance[v] = distance[u] + weight
            change = True
if change:
    result = 1
print(result)