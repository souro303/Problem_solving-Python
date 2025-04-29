n = int(input())
l = list(map(int, input().split()))

count = 0
while True:
    ans = 0
    for i in l:
        count += i
        ans += 1
        if count >= n:
            print(ans)
            break
    if count >= n:
        break


# n=int(input())
# x=list(map(int,input().split()))
# i=0
# while n>x[i]:
#     n-=x[i]
#     i=(i+1)%7
# print(i+1)