# Uses python3
n = int(input())
k = 0
places = [0]
while (n-places[-1]-1 > places[-1]+1):
    k += 1
    places.append(places[-1]+1)
    n -= places[-1]
places.append(n)
print(k+1)
print(*places[1:])