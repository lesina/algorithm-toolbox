# Uses python3
m, n = list(map(int, input().split()))
if n == 0:
    F = [0]
    counter = 0
#elif n == 1:
#    F = [0, 1]
#    print(1)
else:
    F = [0, 1]
    counter = 0
while True:
    F.append((F[-2]+F[-1])%10)
    if F[-2] == 0 and F[-1] == 1:
        F.pop()
        F.pop()
        break
counter = m//len(F) - n//len(F) - 1
m %= len(F)
n %= len(F)
print((sum(F)*counter + sum(F[:n+1]) + sum(F[m:]))%10)

