# Uses python3
m = int(input())
tens = m // 10
fives = (m%10)//5
ones = m%10 - 5*fives
print(tens + fives + ones)
