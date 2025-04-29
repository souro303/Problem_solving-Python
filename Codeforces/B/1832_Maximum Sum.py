for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    arr = sorted(a)
    ar = max(sum(arr[:-k]), sum(arr[2*k:]))
    while k > 0:
        if sum(arr[:-1]) >= sum(arr[2:]):
            arr = arr[:-1]
        else:
            arr = arr[2:]
        k -= 1
    print(max(sum(arr), ar))