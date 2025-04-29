l = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    l.append((a, b))
l.sort
if any(l[i][1] > l[i + 1][1] for i in range(len(l) - 1)):  # Check if quality decreases as price increases
    print("Happy Alex")
else:
    print("Poor Alex")