import math
from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    u = sorted(set(a))  # Unique values in sorted order
    
    for v in u:
        cntB = sum(1 for x in a if x == v)
        cntC = n - cntB
        
        if cntB > 0 and cntC > 0:
            g = 0
            for x in a:
                if x != v:
                    g = x if g == 0 else math.gcd(g, x)
            
            if g != v:
                print("Yes")
                for x in a:
                    print(1 if x == v else 2, end=" ")
                print()
                return
    
    print("No")

t = int(input())
for _ in range(t):
    solve()
