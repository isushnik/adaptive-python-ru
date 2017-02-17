# a = [1, -3, -4, -1, 1]
# a = [1, 3, 5]
# a = [4]
a = [int(i) for i in input().split()]
n = len(a)
b = [abs(a[i] - a[i+1]) for i in range(n-1)]
if sorted(b) == [i for i in range(1, n)]:
    print("Jolly")
else:
    print("Not jolly")




