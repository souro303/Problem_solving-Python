n, a, b, c = map(int, input().split())

List = [a, b, c]
s = sorted(set(List))

ans = 0

while n >= s[0]:
    for i in range(len(s) - 1, -1, -1):
        if n >= s[i]:
            n -= s[i]
            ans += 1
            break

print(ans)
