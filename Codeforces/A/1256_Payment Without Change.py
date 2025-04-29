for _ in range(int(input())):
    a, b, n, s = map(int, input().split())
    
    print('YES' if s%n <= b and (a*n)+b >= s else "NO" )