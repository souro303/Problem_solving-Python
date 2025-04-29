n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
rez = 2 * max(a[0], l - a[-1])

for i in range(n - 1):
    rez = max(rez, a[i + 1] - a[i])

print(f"{rez / 2:.10f}")
