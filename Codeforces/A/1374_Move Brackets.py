for _ in range(int(input())):
    l = []
    a = 0
    n = int(input())
    s = input()
    
    for i in s:
        if i == '(':
            l.append(i)
        else:
            if len(l) > 0:
                l.pop()
            else:
                a += 1
    print(a)