s, n = map(int, input().split())

c = []
for i in range(n):
    x, y = map(int, input().split())
    c.append((x, y))

c.sort()
for x, y in c:
    if s > x:
        s += y
    else:
        print("NO")
        break
else:
    print("YES")

print(c)