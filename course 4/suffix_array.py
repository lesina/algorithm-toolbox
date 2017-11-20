# Uses python3
#
# text = list(input())
# cycles = list()
# length = len(text)
# for i in range(len(text)):
#     cycles.append(text[i:] + text[:i])
# cycles.sort()
# answer = [length-cycles[i].index("$")-1 for i in range(length)]
# print(*answer)

def get_suffix_array(str):
    return sorted(range(len(str)), key=lambda i: str[i:])

text = input()
print(*get_suffix_array(text))