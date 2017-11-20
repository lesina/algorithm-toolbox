# Uses python2
def bw(t):
    m = sorted(t[-i:] + t[:-i] for i in range(len(t)))
    return "".join(m[i][len(t) - 1] for i in range(len(t)))


# for a given string return index with nth occurence of char
def n_occurence_index(string, char, n):
    vector = [string[:index + 1].count(char) for index in range(0, len(string))]
    return vector.index(n)


# tells us how many times a char at given index has occured prior to that char
def occurences(string, index):
    return string[:index + 1].count(string[index])


bwt = raw_input()

# bwt = bw(t)
# print "BW(T) is:", bwt

# reconstruct the t backwards
t = ''
index = 0
first_column = sorted(bwt)

for i in range(len(bwt) - 1):
    char = bwt[index]
    t = char + t
    occurence_count = occurences(bwt, index)
    index = n_occurence_index(first_column, char, occurence_count)

print t + '$'