# scores = ['F', 'B', 'A', 'A', 'B', 'C', 'A', 'D']
# scores = ['B', 'C', 'B']
# scores = ['A', 'D']
scores = input().split()
f = scores.count('A') / len(scores)
print('%.2f' % f)
