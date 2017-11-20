# Uses python3

def bwt(text):
    cycles = list()
    for i in range(len(text)):
        cycles.append(text[i:] + text[:i])
    answer = ""
    cycles.sort()
    for cycle in cycles:
        answer += cycle[-1]
    return answer


text = input()
print(bwt(text))