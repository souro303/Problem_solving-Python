for i in range(int(input())):
    n, x = map(int, input().split())
    a = map(lambda t: int(t) % 2, input().split())
    s = sum(a)
    print("No" if s == 0 or (n - s == 0 and x % 2 == 0) or (n == x and s % 2 == 0) else "Yes")
