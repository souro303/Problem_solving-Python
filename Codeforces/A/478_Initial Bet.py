c1, c2, c3, c4, c5 = map(int, input().split())
c = c1 + c2 + c3 + c4 + c5

if c % 5 == 0 and c>0:
    print(c//5)
else:
    print(-1)