# Uses python3

def merge(A, B):
    Res = []
    i = 0
    j = 0
    o = len(A)
    O = len(B)
    while i < o and j < O:
        if A[i][0] < B[j][0]:
            Res.append(A[i])
            i += 1
        elif A[i][0] > B[j][0]:
            Res.append(B[j])
            j += 1
        elif A[i][1] <= B[j][1]:
            Res.append(A[i])
            i += 1
        elif A[i][1] > B[j][1]:
            Res.append(B[j])
            j += 1
    Res += A[i:] + B[j:]
    return Res


def MergeSort(A):
    if len(A) <= 1:
        return A
    else:
        m = len(A) // 2
        L = MergeSort(A[:m])
        R = MergeSort(A[m:])
    return merge(L, R)


def sortByFirst(inputList):
    return str(inputList[0]) + inputList[1]


s, p = list(map(int, input().split()))
points = []
for i in range(s):
    a, b = list(map(int, input().split()))
    points.append((a, "1"))
    points.append((b, "3"))
numbers = list(map(int, input().split()))
answer = dict()
for i in numbers:
    answer[i] = 0
    points.append((i, "2"))
points = MergeSort(points)
res = 0
for i in points:
    if i[1] == "1":
        res += 1
    elif i[1] == "3":
        res -= 1
    else:
        answer[i[0]] = res
for i in numbers:
    print(answer[i], end=" ")

# for i in range(p):
#     for j in range(s):
#         if points[i] >= segments[j][0] and points[i] <= segments[j][1]:
#             answer[i] += 1
#         else:
#             break

# while points:
#     for segment in segments:
#         if points[0] >= segment[0] and points[0] <= segment[1]:
#             answer += 1
#         else:
#             break
#     print(answer, end=" ")
#     answer = 0
#     points.pop(0)
#     while segments:
#         if points[0] > segments[0][1]:
#             segments.pop()
#         else:
#             break

