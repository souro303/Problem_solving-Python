n = int(input())
a = list(map(int, input().split()))

total_ones = sum(a)
if total_ones == n:
    print(n - 1)
else:
    max_gain = 0
    current_gain = 0
    for num in a:
        gain = 1 if num == 0 else -1
        current_gain = max(gain, current_gain + gain)
        max_gain = max(max_gain, current_gain)
    print(total_ones + max_gain)
