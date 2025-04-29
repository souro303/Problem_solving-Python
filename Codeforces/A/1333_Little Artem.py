# t = int(input())
# for _ in range(t):
#     n, m = map(int, input().split())
#     ans = ''
#     for i in range(n-1):
#         if i % 2 == 0 or i == 0:
#             print('B'*m)
#         else:
#             print('W'*m)
#     if n%2 == 0:
#         print('W'*(m-1)+"B")
#     else:
#         print('B'*(m-1)+"W")