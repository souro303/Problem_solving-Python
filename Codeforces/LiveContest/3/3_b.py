t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = 0
    temp = []
    sort_arr = sorted(arr, reverse=True)
    
    for i in range(len(sort_arr)):
        if sort_arr[i] >= x:
            ans += 1
        else:
            temp.append(sort_arr[i])
            if len(temp)*min(temp) >= x:
                ans += 1
                temp = []
    
    print(ans)
    