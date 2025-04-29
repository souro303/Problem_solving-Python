d = {}
for _ in range(int(input())):
    s = input()
    if s not in d:
        d[s] = 1
    else:
        d[s] += 1
    
mk = max(d, key=d.get)
print(mk)
    