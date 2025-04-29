t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    ones = s.count('1')
    total_ones = ones * (n - 1) + (n - ones) * 1
    print(total_ones)