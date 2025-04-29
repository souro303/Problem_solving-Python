s = input()
d = ['o', 'l', 'l', 'e', 'h']

for i in s:
    if i == d[-1]:
        d.pop()
    if not d:  # Check if the list is empty
        break

if not d:
    print("YES")
else:
    print("NO")
