def is_sum_of_two_cubes(x):
    # Iterate over possible values of a
    a = 1
    while a**3 < x:
        b_cubed = x - a**3
        # Check if b_cubed is a perfect cube
        b = round(b_cubed**(1/3))  # Approximate cube root of b_cubed
        if b > 0 and b**3 == b_cubed:
            return True
        a += 1
    return False

# Read input
t = int(input())

for _ in range(t):
    x = int(input())
    if is_sum_of_two_cubes(x):
        print("YES")
    else:
        print("NO")
