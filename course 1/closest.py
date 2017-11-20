#Uses python3

import math



def closestpair(L):
    def square(x):
        return x * x

    def sqdist(p, q):
        return square(p[0] - q[0]) + square(p[1] - q[1])

    # Work around ridiculous Python inability to change variables in outer scopes
    # by storing a list "best", where best[0] = smallest sqdist found so far and
    # best[1] = pair of points giving that value of sqdist.  Then best itself is never
    # changed, but its elements best[0] and best[1] can be.
    #
    # We use the pair L[0],L[1] as our initial guess at a small distance.
    best = [sqdist(L[0], L[1]), (L[0], L[1])]

    # check whether pair (p,q) forms a closer pair than one seen already
    def testpair(p, q):
        d = sqdist(p, q)
        if d < best[0]:
            best[0] = d
            best[1] = p, q

    # merge two sorted lists by y-coordinate
    def merge(A, B):
        i = 0
        j = 0
        while i < len(A) or j < len(B):
            if j >= len(B) or (i < len(A) and A[i][1] <= B[j][1]):
                yield A[i]
                i += 1
            else:
                yield B[j]
                j += 1

    # Find closest pair recursively; returns all points sorted by y coordinate
    def recur(L):
        if len(L) < 2:
            return L
        split = len(L) // 2
        splitx = L[split][0]
        L = list(merge(recur(L[:split]), recur(L[split:])))

        # Find possible closest pair across split line
        # Note: this is not quite the same as the algorithm described in class, because
        # we use the global minimum distance found so far (best[0]), instead of
        # the best distance found within the recursive calls made by this call to recur().
        # This change reduces the size of E, speeding up the algorithm a little.
        #
        E = [p for p in L if abs(p[0] - splitx) < best[0]]
        for i in range(len(E)):
            for j in range(1, 8):
                if i + j < len(E):
                    testpair(E[i], E[i + j])
        return L

    L.sort()
    recur(L)
    return best[1]







# # Trigger function for closest_pair function
# def closest(P, n):
#     X = list(P)
#     Y = list(P)
#
#     X.sort()
#     Y = sort_y(Y)
#     return closest_pair(X, Y, n)
#
#
# # Recursive Closest Pair function
# def closest_pair(X, Y, n):
#     if n < 3:
#         return brute_force(X, n)
#
#     mid = n // 2
#     Y_Left = []
#     Y_Right = []
#
#     for p in Y:
#         if p in X[:mid]:
#             Y_Left.append(p)
#         else:
#             Y_Right.append(p)
#
#     dis_left = closest_pair(X[:mid], Y_Left, mid)
#     dis_right = closest_pair(X[mid:], Y_Right, n - mid)
#
#     min_dis = min(dis_left, dis_right)
#
#     strip = []
#
#     for (x, y) in Y:
#         if abs(x - X[mid][0]) < min_dis:
#             strip.append((x, y))
#     return min(min_dis, strip_closest(strip, min_dis))
#
#
# # Utility function to calculate min distance between points in strip
# def strip_closest(strip, d):
#     min_d = d
#     for i, (x, y) in enumerate(strip):
#         for j in range(i + 1, len(strip)):
#             if (strip[j][1] - strip[i][1]) < min_d and distance(strip[i], strip[j]) < min_d:
#                 min_d = distance(strip[i], strip[j])
#     return min_d
#
#
# # Calculates the distance between two points
# def distance(a, b):
#     x = a[0] - b[0]
#     y = a[1] - b[1]
#     return math.sqrt(x*x + y*y)
#
#
# # Sort points by x value
# def sort_y(tuples):
#     return sorted(tuples, key=lambda last: last[-1])
#
#
# # Brute force method to calculate distance for n<=3
# def brute_force(X, n):
#     min_d = distance(X[0], X[1])
#
#     for i, (x, y) in enumerate(X):
#         for j in range(i + 1, n):
#             if distance(X[i], X[j]) < min_d:
#                 min_d = distance(X[i], X[j])
#
#     return min_d








n = int(input())
points = []
for i in range(n):
    points.append(tuple(map(int, input().split())))
p1, p2 = closestpair(points)
print(math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2))