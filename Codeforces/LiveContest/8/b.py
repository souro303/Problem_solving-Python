# Educational Codeforces Round 178 (Rated for Div. 2)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    suf = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suf[i] = suf[i + 1] + a[i]

    pref_max = [0] * n
    if n > 0:
        pref_max[0] = a[0]
        for i in range(1, n):
            pref_max[i] = max(pref_max[i - 1], a[i])

    res = []
    for k in range(1, n + 1):
        t1 = suf[n - k]
        t2 = suf[n - k + 1] + pref_max[n - k] if n - k >= 0 else 0
        res.append(max(t1, t2))

    print(*res)

