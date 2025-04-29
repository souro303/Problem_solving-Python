t = int(input())
for _ in range(t):
    n = input().strip()
    
    l = len(n)
    a, b = 0, 0
    for i in range(l):
        if n[i] == '0':
            a += 1
        else:
            b = max(b, a+1)
    print(l-b)
