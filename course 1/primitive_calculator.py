# Uses python3

def calculate(number):
    minNumOperations = [[0,0], [0,0]]
    for n in range(2, number+1):
        minNumOperations.append((float("inf"), 0))
        if not n % 2:
            numOperations = minNumOperations[n // 2][0] + 1
            if numOperations < minNumOperations[n][0]:
                minNumOperations[n] = [numOperations, n//2]
        if not n % 3:
            numOperations = minNumOperations[n // 3][0] + 1
            if numOperations < minNumOperations[n][0]:
                minNumOperations[n] = [numOperations, n//3]
        if n >= 1:
            numOperations = minNumOperations[n - 1][0] + 1
            if numOperations < minNumOperations[n][0]:
                minNumOperations[n] = [numOperations, n-1]
    return minNumOperations


number = int(input())
result = calculate(number)
amount = result[-1][0]
print(amount)
path = [number]
for i in range(amount):
    path.append(result[path[-1]][1])
print(*path[::-1])