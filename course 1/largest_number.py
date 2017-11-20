# Uses python3

def largestNumber(digits):
    answer = ""
    while digits:
        maxDigit = 0
        for digit in digits:
            #EXPERIMENTS
            x = str(digit) + str(maxDigit)
            y = str(maxDigit) + str(digit)
            #if isGreaterOrEqual(digit, maxDigit):
            if x > y:
                maxDigit = digit
        answer += str(maxDigit)
        digits.pop(digits.index(maxDigit))
    return answer


def isGreaterOrEqual(digit, maxDigit):
    MIN = list(str(min(digit, maxDigit)))
    length = len(list(map(int, MIN)))
    if type(digit) == int:
        digit = list(map(int, list(str(digit))))
        maxDigit = list(map(int, list(str(maxDigit))))
    answer = True
    num = 0
    for i in range(length):
        num = i
        if digit[i]<maxDigit[i]:
            answer = False
            break
        elif digit[i]>maxDigit[i]:
            break
    if digit[num] == maxDigit[num]:
        if num < len(digit)-1:
            for i in range(num, len(digit)-1):
                if digit[i+1] < digit[0]:
                    answer = False
                    break
                elif digit[i+1] > digit[0]:
                    answer = True
                    break
        else:
            for i in range(num, len(maxDigit)-1):
                if maxDigit[i+1] < maxDigit[0]:
                    answer = True
                    break
                elif maxDigit[i+1] > maxDigit[0]:
                    answer = False
                    break
    return answer

# import random as rand
# for i in range(10):
#     n = rand.randint(1,100)
#     array = []
#     for i in range(n):
#         array.append(rand.randint(1,1000))
#     array.sort(reverse=True)
#     print(largestNumber(array), end="\n\tOK!!!!!\n\n\n")


n = int(input())
array = list(map(int, input().split()))
array.sort(reverse=True)
print(largestNumber(array))