#Uses python3

def compare(a, b, c, na, nb, nc):
    D = [[[0] * (nb + 1) for i in range(na + 1)] for j in range(nc+1)]
    for i in range(nc+1):
        for j in range(na+1):
            for k in range(nb + 1):
                if i == 0 or j == 0 or k == 0:
                    D[i][j][k] = 0
                elif c[i - 1] == a[j - 1] == b[k - 1]:
                    D[i][j][k] = D[i - 1][j - 1][k - 1] + 1
                else:
                    D[i][j][k] = max(D[i - 1][j][k], D[i][j - 1][k], D[i][j][k-1])
    return D[nc][na][nb]



n = int(input())
sequence1 = list(map(int, input().split()))
m = int(input())
sequence2 = list(map(int, input().split()))
l = int(input())
sequence3 = list(map(int, input().split()))
print(compare(sequence1, sequence2, sequence3, n, m, l))