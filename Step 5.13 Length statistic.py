# string = 'Beautiful is better than ugly. Explicit is better than implicit.'
string = input()
counts = [len(w) for w in string.split()]
lengths = sorted(list(set(counts)))
for e in lengths:
    print('%d: %d' % (e, counts.count(e)))
