t = int(input())
for _ in range(t):
    n, x = map(int, input().split())

    res = list(range(x))
    res += [i for i in range(x + 1, n)]

    if x < n:
        res.append(x)

    print(' '.join(map(str, res)))
