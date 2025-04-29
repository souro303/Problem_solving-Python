for _ in range(int(input())):
    n = int(input())
    s = input()
    
    dash = s.count('-')
    under = s.count('_')
    if dash < 2 or under < 1:
        print(0)
    else:
        half = dash // 2
        print(half * (dash - half) * under)