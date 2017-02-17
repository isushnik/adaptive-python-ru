# a = '3ab4c2Ca12B'
a = input()
i = 0
string = []
while i < len(a):
    j = 0
    while i+j < len(a) and a[i+j].isdigit():
        j += 1
    if j == 0:
        string.append(a[i])
    else:
        string.append(int(a[i:i+j]) * a[i+j])
    i += j + 1

print(''.join(string))
