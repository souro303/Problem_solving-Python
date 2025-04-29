n = int(input())

list = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]

# while n > 0:
#     list.append(list[0])
#     list.append(list[0])
#     list.pop(0)
#     n -= 1
# print(list[-1])

round_size = 5
while n > round_size:
    n -= round_size
    round_size *= 2

person_index = (n - 1) // (round_size // 5)
print(list[person_index])
