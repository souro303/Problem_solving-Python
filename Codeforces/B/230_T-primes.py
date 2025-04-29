from math import isqrt

MAX = 1000000

def precompute_t_primes():
    is_prime = [True] * (MAX + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, isqrt(MAX) + 1):
        if is_prime[i]:
            for j in range(i * i, MAX + 1, i):
                is_prime[j] = False

    return {i * i for i in range(2, MAX + 1) if is_prime[i]}

t_primes = precompute_t_primes()

input()
numbers = map(int, input().split())

for num in numbers:
    print("YES" if num in t_primes else "NO")
