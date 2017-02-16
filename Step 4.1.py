string = input()
i = 0
res = ''
while i < len(string):
    s = string[i]
    j = 1
    while i+j < len(string) and string[i+j] == s:
        j += 1
    if j > 1:
        res += str(j)
    res += s
    i += j

print(res)
