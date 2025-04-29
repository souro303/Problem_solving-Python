# l = []
# for i in range(int(input())):
#     name = input()
#     if name not in l:
#         l.append(name)
#         print('OK')
#     else:
#         j = 1
#         while f"{name}{j}" in l:
#             j += 1
#         name = f"{name}{j}"
#         l.append(name)
#         print(name)
        
name_count = {}
for _ in range(int(input())):
    name = input()
    if name not in name_count:
        name_count[name] = 0
        print("OK")
    else:
        name_count[name] += 1
        unique_name = f"{name}{name_count[name]}"
        name_count[unique_name] = 0 
        print(unique_name)
