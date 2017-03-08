# n, m = (int(i) for i in input().split())
# field = [[c for c in input()] for _ in range(n)]
n = 5  # rows
m = 5  # columns
field = [['.', '.', '.', '.', '.'],
         ['.', '.', 'X', '.', '.'],
         ['.', '.', '.', 'X', '.'],
         ['.', 'X', 'X', 'X', '.'],
         ['.', '.', '.', '.', '.']]

live = 'X'
dead = '.'


def neighbors(k, l):
    global field
    s = 0 if field[k][l] == live else -1
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if field[(k+i) % n][(l+j) % m] == live:
                s += 1
    return s

nextg = [[field[i][j] for j in range(m)] for i in range(n)]

for k in range(n):
    for l in range(m):
        nbrs = neighbors(k, l)
        if field[k][l] == dead and nbrs == 3:
            nextg[k][l] = live
        if field[k][l] == live and (nbrs < 2 or nbrs > 3):
            nextg[k][l] = dead

for line in nextg:
    print(''.join(line))
