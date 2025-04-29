n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
if k == 0:
    if a[0] > 1:
        print(a[0]-1)
    else:
        print(-1)

if k > 0:
    x = a[k-1]
    
    count = sum(1 for i in a if i <= x)
    if count == k:
        print(x)
    else:
        print(-1)