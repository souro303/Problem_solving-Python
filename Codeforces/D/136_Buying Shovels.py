def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:  # Avoid duplicate factors
                factors.append(n // i)
    return sorted(factors, reverse=True)

for _ in range(int(input())):
    n, k = map(int, input().split())
    l = find_factors(n)
    length = len(l)
    ans = 1
    for i in range(length):
        if l[i] <= k:
            ans = n//l[i]
            break
    print(ans)
