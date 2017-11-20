# Uses python3


def knapsack(w, capacity):
    value = [[0]*(len(w)+1)]
    for i in range(capacity):
        value.append([0]*(len(w)+1))
    for i in range(1, len(w)+1):
        for j in range(1, capacity+1):
            value[j][i] = value[j][i-1]
            if w[i-1] <= j:
                val = value[j-w[i-1]][i-1] + w[i-1]
                if value[j][i] < val:
                    value[j][i] = val
    return value[-1][-1]



W, n = list(map(int, input().split()))
w = list(map(int, input().split()))
print(knapsack(w, W))

# import random
# for j in range(100):
#     W = random.randint(1, 1000)
#     n = random.randint(1, 300)
#     w = []
#     for i in range(n):
#         w.append(random.randint(0, 10000))
#     print(knapsack(w, W))