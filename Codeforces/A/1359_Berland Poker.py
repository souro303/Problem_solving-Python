t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    d = n // k
    a1 = min(m, d)
    a2 = (m - a1 + k - 2) // (k - 1)
    print(a1 - a2)