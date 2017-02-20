def modify_list(l):
    m = l.copy()
    l.clear()
    l.extend([int(e/2) for e in m if e % 2 == 0])

# lst = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]

# lst = [10, 5, 8, 3]
# modify_list(lst)
# print(lst)               # [5, 4]
