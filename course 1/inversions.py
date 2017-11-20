#Uses python3

def merge(A, B, N):
    Res = []
    i = 0
    j = 0
    o = len(A)
    oo = o
    O = len(B)
    while i < o and j < O:
        if A[i] <= B[j]:
            Res.append(A[i])
            i += 1
            oo -= 1
        else:
            Res.append(B[j])
            j += 1
            N += 1*oo
    Res += A[i:] + B[j:]
    return Res, N


def MergeSort(A, N):
    if len(A) <= 1:
        return A, N
    else:
        m = len(A) // 2
        L, N = MergeSort(A[:m], N)
        R, N = MergeSort(A[m:], N)
    return merge(L, R, N)


n = int(input())
array = list(map(int, input().split()))
print(MergeSort(array, 0)[1])