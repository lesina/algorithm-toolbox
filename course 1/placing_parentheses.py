# Uses python3

def minAndMax(i, j, m, M):
    MIN = float('inf')
    MAX = -float('inf')
    for k in range(i, j):
        if operations[k] == "+":
            a = M[i][k] + M[k+1][j]
            b = M[i][k] + m[k+1][j]
            c = m[i][k] + M[k+1][j]
            d = m[i][k] + m[k+1][j]
            MIN = min(MIN, a, b, c, d)
            MAX = max(MAX, a, b, c, d)
        elif operations[k] == "-":
            a = M[i][k] - M[k+1][j]
            b = M[i][k] - m[k+1][j]
            c = m[i][k] - M[k+1][j]
            d = m[i][k] - m[k+1][j]
            MIN = min(MIN, a, b, c, d)
            MAX = max(MAX, a, b, c, d)
        elif operations[k] == "*":
            a = M[i][k] * M[k+1][j]
            b = M[i][k] * m[k+1][j]
            c = m[i][k] * M[k+1][j]
            d = m[i][k] * m[k+1][j]
            MIN = min(MIN, a, b, c, d)
            MAX = max(MAX, a, b, c, d)
    return (MIN, MAX)



def parentheses(numbers):
    m = [[0]*len(numbers)]
    M = [[0]*len(numbers)]
    for i in range(len(numbers)-1):
        m.append([0]*len(numbers))
        M.append([0] * len(numbers))
    for i in range(len(numbers)):
        m[i][i] = int(numbers[i])
        M[i][i] = int(numbers[i])
    for s in range(1, len(numbers)):
        for i in range(len(numbers)-s):
            j = i+s
            m[i][j], M[i][j] = minAndMax(i, j, m, M)
    return M[0][len(numbers)-1]


expression = list(input())
operations = [x for x in expression[1::2]]
numbers = [x for x in expression[0::2]]
print(parentheses(numbers))