n = int(input())
while n > 0:
    s = input()
    res = 0 
    cur = 0  
    min_cur = 0 
    for char in s:
        if char == '+':
            cur += 1
        else:  # char == '-'
            cur -= 1
        res += 1  # Count every step
        if cur < 0:
            # Add additional steps for the required `init`
            res += abs(cur)
            cur = 0  # Reset to 0 to ensure no negatives
            min_cur = min(min_cur, cur)
    print(res)
    n -= 1