# Uses python3
n, m = list(map(int, input().split()))
F = [0, 1]
for i in range(n-1):
    F.append((F[-1]+F[-2])%m)
    if F[-2] == 0 and F[-1] == 1:
        F.pop()
        F.pop()
        n = n%len(F)
        break
print(F[n])
