# Uses python3
# n, W = list(map(int, input().split()))
# valuable = dict()
# for i in range(n):
#     v, w = list(map(int, input().split()))
#     if v/w in valuable:
#         valuable[v/w][0] += v
#         valuable[v/w][1] += w
#     else:
#         valuable[v/w] = [v, w]
# keys = sorted(valuable, reverse = True)
# answer = 0
# for key in keys:
#     if not valuable[key][1] // W:
#         answer += valuable[key][0]
#     else:
#         answer += key*W
#     W -= valuable[key][1]
#     if W <= 0:
#         break
# print(round(answer, 4))

# import random as rand
# while True:
#     n = rand.randint(0, 1000)
#     W = rand.randint(0, 2000000)
#     valuable = dict()
#     for i in range(n):
#         v = rand.randint(0, 2000000)
#         w = rand.randint(1, 2000000)
#         if v / w in valuable:
#             valuable[v / w][0] += v
#             valuable[v / w][1] += w
#         else:
#             valuable[v / w] = [v, w]
#     keys = sorted(valuable, reverse=True)
#     print("The last shit: ", valuable, end = '\n\n')
#     answer = 0
#     for key in keys:
#         if not valuable[key][1] // W:
#             answer += valuable[key][0]
#         else:
#             answer += key * W
#         W -= valuable[key][1]
#         if W <= 0:
#             break
#     print("OK!!!!!!!!!!!!", end="\n\n\n\n\n")

def sortByFract(inputList):
    return inputList[0]/inputList[1]


def knapsack(W, items):
    V = 0
    for i in items:
        if W == 0:
            return V
        a = min(i[1], W)
        V += a * (i[0]/i[1])
        i[0] -= a
        W -= a
    return V


n, W = list(map(int, input().split()))
valuable = []
for i in range(n):
    v, w = list(map(int, input().split()))
    valuable.append([v, w])
valuable.sort(key=sortByFract, reverse=True)
print(round(knapsack(W, valuable), 4))