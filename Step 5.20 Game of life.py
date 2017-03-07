# n = 5  # rows
# m = 5  # columns
# field = [['.', '.', '.', '.', '.'],
#          ['.', '.', 'X', '.', '.'],
#          ['.', '.', '.', 'X', '.'],
#          ['.', 'X', 'X', 'X', '.'],
#          ['.', '.', '.', '.', '.']]
n, m = (int(i) for i in input().split())
# print(n, m)
field = [[c for c in input()] for _ in range(n)]
# for line in field:
#     print(''.join(line))
#

live = 'X'
dead = '.'


def neighbors(k, l):
    global field
    s = 0
    # print(field[k][l])
    if field[k][l] == live:
        s = -1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if field[(k+i) % n][(l+j) % m] == live:
                s += 1
    return s

# print(neighbors(1, 1))  # 1
# print(neighbors(3, 3))  # 2
# print(neighbors(3, 4))  # 2
# print(neighbors(1, 2))  # 1
# print(neighbors(4, 2))  # 3

nextg = [[field[i][j] for j in range(m)] for i in range(n)]

for k in range(n):
    for l in range(m):
        nbrs = neighbors(k, l)
        # print(k, l, nbrs)
        if field[k][l] == dead and nbrs == 3:
            nextg[k][l] = live
        if field[k][l] == live:
            if nbrs < 2 or nbrs > 3:
                nextg[k][l] = dead

# print('---------')
for line in nextg:
    print(''.join(line))
