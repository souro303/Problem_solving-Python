t = int(input())
for _ in range(t):
    s = list(input().strip())
    t = input().strip()
    idx = 0
    
    for i in range(len(s)):
        if s[i] == '?':
            if idx < len(t):
                s[i] = t[idx]
                idx += 1
            else:
                s[i] = 'a'
        elif idx < len(t) and s[i] == t[idx]:
            idx += 1
        
    if idx >= len(t):
        print('YES')
        print("".join(s))
    else:
        print("NO")