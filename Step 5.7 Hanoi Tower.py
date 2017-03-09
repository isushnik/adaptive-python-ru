def move(i: int, j: int):
    if len(pigs[i]) == 0:
        pigs[i].append(pigs[j].pop())
        print(j+1, '-', i+1)
    elif len(pigs[j]) == 0:
        pigs[j].append(pigs[i].pop())
        print(i+1, '-', j+1)
    elif pigs[i][-1] > pigs[j][-1]:
        pigs[i].append(pigs[j].pop())
        print(j+1, '-', i+1)
    elif pigs[j][-1] > pigs[i][-1]:
        pigs[j].append(pigs[i].pop())
        print(i+1, '-', j+1)


# n = int(input())
n = 3
pigs = [[i for i in range(n, 0, -1)], [], []]

if n % 2 == 0:
    steps = [[0, 1], [0, 2], [1, 2]]
else:
    steps = [[0, 2], [0, 1], [1, 2]]

print(pigs)
while len(pigs[-1]) != n:
    for s in steps:
        if len(pigs[-1]) != n:
            move(*s)

print(pigs)
