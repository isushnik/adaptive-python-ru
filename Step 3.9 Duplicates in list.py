lst = [int(e) for e in input().split()]
print(*[e for e in sorted(set(lst)) if lst.count(e) > 1])
