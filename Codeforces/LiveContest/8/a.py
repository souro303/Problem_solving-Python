# Educational Codeforces Round 178 (Rated for Div. 2)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    t = a + b + c
    if t % 3 != 0:
        print("NO")
    else:
        k = t // 3
        if k >= b:
            print("YES")
        else:
            print("NO")