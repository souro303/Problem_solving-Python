for _ in range(int(input())):
    n, m, l, r = map(int, input().split())
    a = n - m
    
    while a > 0:
        if l < 0:
            l += 1
            a -= 1
        else:
            r -= 1
            a -= 1
    print(l, r)