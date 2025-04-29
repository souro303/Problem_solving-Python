# def find_factors(n):
#     factors = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             factors.append(i)
#             if i != n // i:  # Avoid duplicate factors
#                 factors.append(n // i)
#     return sorted(factors)

# n, x = map(int, input().split())
# l = find_factors(x)

# ans = 0
# for a in l:
#     b = x // a
#     if a > n or b > n:
#         continue
#     if a == b:
#         ans += 1  # Count (a, a) only once
#     elif a < b:
#         ans += 2  # Count (a, b) and (b, a)

# print(ans)


n,x=map(int,input().split())
print(sum((x%i==0 and x/i<=n)for i in range(1,n+1)))