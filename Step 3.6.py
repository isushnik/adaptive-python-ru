n = int(input())

res = []
i = 1
while len(res) < n:
    res.extend(i for j in range(i))
    i += 1

print(*res[:n])
