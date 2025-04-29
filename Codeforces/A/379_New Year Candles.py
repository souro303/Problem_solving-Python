a, b = map(int, input().split())

ans = a
old = a

while True:
    new = old // b
    ans += new
    old = new + (old % b)
    if old < b:
        break

print(ans)