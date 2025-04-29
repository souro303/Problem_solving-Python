n = int(input())
a = list(map(int, input().split()))

s = sorted(a)

start, end = 0, n - 1

while start < n and a[start] == s[start]:
    start += 1

while end > start and a[end] == s[end]:
    end -= 1

# Check if reversing the segment [start:end+1] sorts the array
if s == a:
    print('yes')
    print(1, 1)
elif a[start:end+1][::-1] == s[start:end+1]:
    print("yes")
    print(start+1, end+1)
else:
    print("no")
