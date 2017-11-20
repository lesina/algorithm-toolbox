# Uses python3

def prefix(string):
    v = [0]*len(string)
    for i in range(1,len(string)):
        k = v[i-1]
        while k > 0 and string[k] != string[i]:
            k = v[k-1]
        if string[k] == string[i]:
            k += 1
        v[i] = k
    return v

def kmp(string,substring):
    string = substring + '&' + string
    valuePref = prefix(string)
    answer = []
    for i in range(len(valuePref)):
        if (valuePref[i] == len(substring)):
            index = i - 2 * len(substring)
            answer.append(index)
    return answer

substring = input()
string = input()
print(*kmp(string, substring))
