# Uses python3

def binarySearch(array, pattern, low, high):
    mid = (high + low)//2
    if high <= low and pattern != array[mid]:
        return -1
    if pattern > array[mid]:
        return binarySearch(array, pattern, low=mid+1, high=high)
    elif pattern < array[mid]:
        return binarySearch(array, pattern, low=low, high=mid-1)
    else:
        return mid


a = list(map(int, input().split()))
n = a[0]
a = a[1:]
b = list(map(int, input().split()))
k = b[0]
b = b[1:]
for i in range(k):
    print(binarySearch(a, b[i], low=0, high=n-1), end=" ")