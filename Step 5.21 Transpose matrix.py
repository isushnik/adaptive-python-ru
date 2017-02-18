n, m = [int(i) for i in input().split()]
res = [[0 for _ in range(n)] for _ in range(m)]

for i in range(n):
    row = [int(i) for i in input().split()]
    for j in range(m):
        res[j][i] = row[j]

for e in res:
    print(*e)
