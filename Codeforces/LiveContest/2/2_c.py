t = int(input())
result = []

for _ in range(t):
    n, x = map(int, input().split())
    if n == 1:
        result.append(str(x))
        continue

    a = list(range(n - 1))
    last_element = x

    for num in a:
        last_element ^= num

    if last_element >= n - 1 or last_element > x:
        a[-1] ^= x
        a.append(x)
    else:
        a.append(last_element)

    result.append(' '.join(map(str, a)))

print('\n'.join(result))
