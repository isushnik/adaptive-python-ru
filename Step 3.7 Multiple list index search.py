l = [int(i) for i in input().split()]
n = int(input())
res = [i for i in range(len(l)) if l[i] == n]

if len(res) == 0:
    print(None)
else:
    print(*res)
