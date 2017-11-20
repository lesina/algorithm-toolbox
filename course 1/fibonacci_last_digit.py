# Uses python3
n = int(input())
F = [0, 1]
for i in range(n-1):
    F.append((F[-1]+F[-2])%10)
print(F[n])
