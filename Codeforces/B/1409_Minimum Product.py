for _ in range(int(input())):
    a, b, x, y, n = map(int, input().split())
    ans = float('inf')  # Initialize with a very large value

    for _ in range(2):
        da = min(n, a - x)
        db = min(n - da, b - y)
        ans = min(ans, (a - da) * (b - db))
        a, b = b, a
        x, y = y, x

    print(ans)