for _ in range(int(input())):
    ans = 0
    n = int(input())
    arr = list(map(int, input().split()))
    store = [0, 1, 0, 3, 2, 0, 2, 5]
    for i in range(len(arr)):
        if arr[i] in store:
            store.remove(arr[i])
        if len(store)==0:
            print(i+1)
            break
    else:
        print(ans)