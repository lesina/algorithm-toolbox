# Uses python3
m, n = list(map(int, input().split()))
if n == 0:
    F = [0]
    answer = 0
else:
    F = [0, 1]
    answer = 1
for i in range(m):
    F.append((F[-1]+F[-2])%10)
for i in range(m, n-1):
    F.append((F[-1]+F[-2])%10)
    answer += F[-1]
    answer %= 10
print(answer)
