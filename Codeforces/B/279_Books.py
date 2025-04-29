n, t = map(int, input().split())
l = list(map(int, input().split()))


a, ans = 0, 0
for i in l:
    a += i
    if a <= t:
        ans += 1
    else:
        a -= i
        break
    
books = sorted(l[ans:])
for i in books:
    a += i
    if a <= t:
        ans += 1
    else:
        break
print(ans)