from collections import Counter

n = int(input())

l = []
for _ in range(n):
    h, m = map(int, input().split())
    l.append((h, m))

time_counts = Counter(l)
print(time_counts)

max_count = max(time_counts.values())

print(max_count) 
