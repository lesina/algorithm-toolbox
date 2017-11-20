# Uses python3

def editDistance(A, B):
    leng = len(B)
    D = [[0] * (leng+1)]
    for i in range(len(A)):
        D.append([0]*(leng+1))
    for i in range(len(A)+1):
        D[i][0] = i
    for i in range(len(B)+1):
        D[0][i] = i
    for j in range(1, len(B)+1):
        for i in range(1, len(A)+1):
            insertion = D[i][j-1]+1
            deletion = D[i-1][j]+1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1] + 1
            if A[i-1] == B[j-1]:
                D[i][j] = min(insertion, deletion, match)
            else:
                D[i][j] = min(insertion, deletion, mismatch)
    return D[-1][-1]

A = list(input())
B = list(input())
print(editDistance(A, B))