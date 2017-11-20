#Uses python3

n = int(input())
book = dict()
for i in range(n):
    task = input()
    if task[:4] == "find":
        task, number = task.split()
        if number not in book:
            print("not found")
        else:
            print(book[number])
    elif task[:3] == "add":
        task, number, name = task.split()
        book[number] = name
    else:
        task, number = task.split()
        if number in book:
            book.pop(number)