string, substring = input().strip(), input().strip()

n = len(substring)
res = [i for i in range(len(string) - n + 1) if string[i:i+n] == substring]
if not res:
    print(-1)
else:
    print(*res)
