n, m = map(int, input().split())
l = {}
for i in range(m):
    s = input().split()
    shorter, longer = (s[0], s[1]) if len(s[0]) <= len(s[1]) else (s[1], s[0])
    l[s[0]] = shorter
    l[s[1]] = shorter

ps = input().split()
ans = []
for i in ps:
    if i in l:
        ans.append(l[i])
    else:
        ans.append(i)
print(" ".join(ans))