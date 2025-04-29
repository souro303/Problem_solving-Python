n = int(input())
l = list(map(int, input().split()))

change_25, change_50 = 0, 0  
success = True

for i in l:
    if i == 25:
        change_25 += 1
    elif i == 50:
        if change_25 > 0:
            change_25 -= 1
            change_50 += 1
        else:
            success = False
            break
    elif i == 100:
        if change_50 > 0 and change_25 > 0: 
            change_50 -= 1
            change_25 -= 1
        elif change_25 >= 3: 
            change_25 -= 3
        else:
            success = False
            break

print("YES" if success else "NO")
