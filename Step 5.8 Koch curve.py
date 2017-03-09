def koch(n):
    angles = [60, -120, 60]
    if n == 1:
        return angles
    else:
        kch = koch(n-1)
        res = []
        for i in range(7):
            if i % 2 == 0:
                res.extend(kch)
            else:
                res.append(angles[(i - 1) // 2])
        return res

res = koch(int(input()))
for a in res:
    print('turn', a)
