# Uses python3
def sortByRight(inputList):
    return inputList[1]


n = int(input())
segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))
segments.sort(key=sortByRight)
m = 1
points = [segments[0][1]]
for i in range(1, n):
    if points[-1] < segments[i][0] or points[-1] > segments[i][1]:
        m += 1
        points.append(segments[i][1])
print(m)
print(*points)