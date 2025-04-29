t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    x_fixed = -1
    valid = True
    min_x, max_x = 0, 10**18  # wide range initially

    for i in range(n):
        if b[i] != -1:
            x_i = a[i] + b[i]
            if x_fixed == -1:
                x_fixed = x_i
            elif x_fixed != x_i:
                valid = False
                break
        else:
            min_x = max(min_x, a[i])
            max_x = min(max_x, a[i] + k)

    if not valid:
        print(0)
    else:
        if x_fixed != -1:
            if min_x <= x_fixed <= max_x:
                print(1)
            else:
                print(0)
        else:
            print(max(0, max_x - min_x + 1))
