n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = {}
for i in range(n):
    s[i + 1] = (arr[i] // m, arr[i] % m)  # Store (complete rounds, remaining candies)

max_value = (-1, -1)  # Initialize with a minimum tuple
last_max_child = -1   # Initialize the index of the last max child

for child, value in s.items():
    if value >= max_value:  # Update if current value is greater or equal to max_value
        max_value = value
        last_max_child = child

print(last_max_child)