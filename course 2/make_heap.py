#Uses python3


def parent(i):
    return i//2


def leftChild(i):
    return 2*i+1


def rightChild(i):
    return 2*i+2


def siftDown(index):
    maxIndex = index
    l = leftChild(index)
    if l <= n-1 and array[l] < array[maxIndex]:
        maxIndex = l
    r = rightChild(index)
    if r <= n-1 and array[r] < array[maxIndex]:
        maxIndex = r
    if index != maxIndex:
        changes.append((index, maxIndex))
        array[index], array[maxIndex] = array[maxIndex], array[index]
        siftDown(maxIndex)


def buildHeap(size):
    for i in range(size//2, -1, -1):
        siftDown(i)


n = int(input())
array = list(map(int, input().split()))
changes = list()
buildHeap(n)
length = len(changes)
print(length)
for i in range(length):
    print(*changes[i])