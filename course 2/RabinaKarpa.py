#Uses python3

substring = input()
len_sub = len(substring)
string = input()
len_str = len(string)
hash_sub = 0
hash_str = 0
for i in range(len_sub - 1):
    hash_str += ord(string[i])
for i in range(len_sub):
    hash_sub += ord(substring[i])
for i in range(len_str - len_sub + 1):
    if (len_str - len_sub - i + 1 != 0):
        hash_str += ord(string[i + len_sub - 1])
        if (hash_sub == hash_str):
            j = 0
            if substring == string[i:i+len_sub]:
                print(i, end=" ")
            # while (substring[j] == string[i + j]):
            #     j += 1
            #     if (j == len_sub - 1):
            #         print(i, end=" ")
            #         break
        hash_str -= ord(string[i])
