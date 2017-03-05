words = input().strip()
words = [w.lower() for w in words.split()]
d = {w: words.count(w) for w in set(words)}
for word, count in d.items():
    print(word, count)
