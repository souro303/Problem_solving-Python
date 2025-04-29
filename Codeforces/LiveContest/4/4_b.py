def count_valid_positions(n, k, x, a):
    cycle_sum = sum(a)  # Sum of one cycle of `a`
    
    # If even the full `b` sum is less than `x`, return 0
    if cycle_sum * k < x:
        return 0

    total_valid_positions = 0
    current_sum = 0
    right = 0
    length = n * k  # Total length of `b`

    # Sliding window approach
    for left in range(length):
        while right < length and current_sum < x:
            current_sum += a[right % n]  # Access `b` via modulo
            right += 1

        if current_sum >= x:
            total_valid_positions += length - right + 1

        current_sum -= a[left % n]  # Move left pointer

    return total_valid_positions

# Read input normally
t = int(input())  # Number of test cases
results = []

for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    results.append(str(count_valid_positions(n, k, x, a)))

# Print all results
print("\n".join(results))
