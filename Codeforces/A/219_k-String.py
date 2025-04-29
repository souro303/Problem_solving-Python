from collections import Counter

k = int(input())
s = input()
freq = Counter(s)

base_unit = []
for char, count in freq.items():
    if count % k != 0:
        print(-1)
        exit()  # Exit early if not feasible
    base_unit.append(char * (count // k))

# Construct the k-string
print("".join(base_unit) * k)
