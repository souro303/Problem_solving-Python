from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    freq = Counter(arr)  # Count frequency of elements
    max_count = max(freq.values())  # Find max frequency
    print(min(n - max_count, (n + 1) // 2))
