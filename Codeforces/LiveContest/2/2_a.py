t = int(input())
for i in range(t):
    n, k, p = map(int, input().split())
    
    min_sum = n * (-p)
    max_sum = n * p
    
    if k < min_sum or k > max_sum:
        print(-1)
    
    elif k == 0:
        print(0)
      
    else:
        print((abs(k) + p - 1) // p)
