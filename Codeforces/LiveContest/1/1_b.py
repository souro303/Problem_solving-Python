t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
        
    unique = {num for num in a if freq[num] == 1}
    if not unique:
        print(0)
        continue
    max_len = current_len = best_start = best_end = current_start = 0
    for i in range(n):
        if a[i] in unique:
            current_len += 1
            if current_len > max_len:
                max_len = current_len
                best_start = current_start
                best_end = i
        else:
            current_len = 0
            current_start = i + 1
            
    print(best_start + 1, best_end + 1)
