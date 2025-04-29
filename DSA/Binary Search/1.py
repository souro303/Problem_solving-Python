def search(arr, n):
    l = 0
    u = len(arr) - 1

    while l <= u:
        mid = (l + u) // 2

        if arr[mid] == n:
            return mid  # Return the index, not the value
        elif arr[mid] < n:
            l = mid + 1  # Move the lower bound up
        else:
            u = mid - 1  # Move the upper bound down

    return -1  # Return -1 if the element is not found

arr = [1, 3, 5, 6, 7]
print(search(arr, 3))  # Output: 1
