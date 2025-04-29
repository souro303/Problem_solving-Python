n = int(input())
 
for i in range(n + 2):
        # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers increasing
    for j in range(i):
        print(j, end=" ")
    # Print numbers decreasing
    for j in range(i - 2, -1, -1):
        print(j, end=" ")
    print()
for i in range(n - 1, -1, -1):
    # Print leading spaces
    print(" " * (n - i), end="")
    # Print numbers increasing
    for j in range(i):
        print(j, end=" ")
    # Print numbers decreasing
    for j in range(i - 2, -1, -1):
        print(j, end=" ")
    print()    