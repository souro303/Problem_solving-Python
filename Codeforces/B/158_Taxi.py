# from math import ceil

# n = int(input())
# s = list(map(int, input().split()))

# print(ceil(sum(s)/4))

from math import ceil

n = int(input())
groups = list(map(int, input().split()))

ones = groups.count(1)
twos = groups.count(2)
threes = groups.count(3)
fours = groups.count(4)

taxis = fours

taxis += threes
ones = max(0, ones - threes)

taxis += twos // 2
if twos % 2:
    taxis += 1
    ones = max(0, ones - 2)

# Remaining ones: four per taxi
taxis += ceil(ones / 4)

print(taxis)
