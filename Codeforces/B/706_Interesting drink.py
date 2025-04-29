MAX_COIN = 100000

n = int(input())
x = map(int, input().split())
q = int(input())
m = [int(input()) for _ in range(q)]

count = [0] * (MAX_COIN + 1)

for i in x:
    count[i] += 1

prefix = [0] * (MAX_COIN+1)

for i in range(1, MAX_COIN+1):
    prefix[i] = prefix[i-1] + count[i]

for i in m:
    print(n if i>=MAX_COIN else prefix[i])