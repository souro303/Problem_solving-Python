for _ in range(int(input())):
    a1, a2, b1, b2 = map(int, input().split())
    if a1 == a2 == b1 == b2:
        print(0)
    elif max(a1, a2) >= max(b1, b2) and min(a1, a2) > min(b1, b2) and min(a1, a2) > max(b1, b2):
        print(4)
    elif max(a1, a2) >= max(b1, b2) and min(a1, a2) >= min(b1, b2) and min(a1, a2) > max(b1, b2):
        print(4)
    elif max(a1, a2) >= max(b1, b2) and min(a1, a2) >= min(b1, b2) and min(a1, a2) >= max(b1, b2):
        print(4)
    elif (a1 >= b1 and a2 > b2) or (a1 > b1 and a2 >= b2) or (a1 > b1 and a2 >= b2) or (a1 >= b2 and a2 > b1):
        print(2)
    else:
        print(0)
        
        
    