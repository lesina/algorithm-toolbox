# Uses python3
def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b, a%b)

a, b = list(map(int, input().split()))
if a < b:
    a, b = b, a
print(gcd(a,b))
