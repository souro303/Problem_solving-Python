t = int(input())
for _ in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        res = []
        for x in range(1, n+1):
            if x == n:
                res.append(n)
            else:
                val = (2 * x) % n
                res.append(val)
        print(' '.join(map(str, res)))