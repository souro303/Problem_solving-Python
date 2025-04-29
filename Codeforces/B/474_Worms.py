import bisect

n = int(input())
arr = map(int, input().split())
m = int(input())
q = map(int, input().split())

temp = []
a = 0
for i in arr:
    a += i
    temp.append(a)

for num in q:
    idx = bisect.bisect_left(temp, num)
    print(idx + 1)