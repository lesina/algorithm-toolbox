# Uses python3
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
answer = a[0]*b[0]
for i in range(1, n):
    answer += a[i]*b[i]
print(answer)