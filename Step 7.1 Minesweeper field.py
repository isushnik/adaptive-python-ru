n, m = (int(i) for i in input().split())
# n, m = 4, 4

field = [list(input()) for _ in range(n)]
# field = [['.', '.', '*', '.'], ['*', '*', '.', '.'], ['.', '.', '*', '.'], ['.', '.', '.', '.']]
# print(field)
answer = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        # print('i:', i, 'j:', j)
        if field[i][j] == '*':
            answer[i][j] = '*'
            # print('mine')
        else:
            for k in [i-1, i, i+1]:
                if k < 0 or k > n-1:
                    continue
                for l in [j-1, j, j+1]:
                    if l < 0 or l > m - 1:
                        continue
                    # print('k:', k, 'l:', l)
                    if k == i and l == j:
                        continue
                    if field[k][l] == '*':
                        answer[i][j] += 1

# print(answer)

for e in answer:
    print(''.join([str(i) for i in e]))
