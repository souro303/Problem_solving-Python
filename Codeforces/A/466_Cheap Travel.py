n, m, a, b = map(int, input().split())

l = []

if n % m == 0:
    l.append(int(n/m)*b)

l.append(n*a)
l.append((n // m) * b + (n % m) * a)
l.append(((n//m)+1)*b)

print(min(l))