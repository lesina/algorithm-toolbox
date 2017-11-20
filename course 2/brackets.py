# Uses python3

brackets = list(input())
indicator = 0
stack = []
nothingToDo = False
indexesOfOpened = []
for i in range(len(brackets)):
    stack.append(brackets[i])
    if stack[-1] == "(" or stack[-1] == "[" or stack[-1] == "{":
        indicator += 1
        indexesOfOpened.append(i)
    elif stack[-1] not in "()[]{}":
        stack.pop()
    elif len(stack) == 1 and (stack[-1] == ")" or stack[-1] == "]" or stack[-1] == "}"):
        print(i+1)
        nothingToDo = True
        break
    elif len(stack) >= 2 and ("".join(stack[-2:])!="()" and "".join(stack[-2:])!="[]" and "".join(stack[-2:])!="{}"):
        print(i+1)
        nothingToDo = True
        break
    elif stack[-1] == ")" and stack[-2] == "(":
        stack.pop()
        stack.pop()
        indexesOfOpened.pop()
        indicator -= 1
    elif stack[-1] == "]" and stack[-2] == "[":
        stack.pop()
        stack.pop()
        indexesOfOpened.pop()
        indicator -= 1
    elif stack[-1] == "}" and stack[-2] == "{":
        stack.pop()
        stack.pop()
        indexesOfOpened.pop()
        indicator -= 1
    elif indicator < 0:
        print(i+1)
        nothingToDo = True
        break
    else:
        print(i+1)
        nothingToDo = True
        break
if not indicator and not stack:
    print("Success")
elif not nothingToDo:
    print(indexesOfOpened[0]+1)
# elif indexesOfOpened:
#     print(indexesOfOpened[0]+1)