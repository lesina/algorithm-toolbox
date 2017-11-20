# Uses python3


def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

n, m = list(map(int, input().split()))
rank = [0] + list(map(int, input().split()))
parent = [i for i in range(n + 1)]
current_max = max(rank)

for source, dest in (list(map(int, input().split())) for i in range(m)):
    source, dest = find_parent(source), find_parent(dest)
    if source != dest:
        if rank[source] > rank[dest]:
            source, dest = dest, source
        parent[source] = dest
        rank[dest] += rank[source]

    current_max = max(current_max, rank[dest])
    print(current_max)