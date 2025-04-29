n, m = map(int, input().split())
arr = list(map(int, input().split()))

ans = arr[0] - 1

for i in range(m-1):
    if arr[i] <= arr[i + 1]:
        ans += arr[i + 1] - arr[i]
    else:
        ans += (n - arr[i]) + arr[i + 1]

print(ans)
        