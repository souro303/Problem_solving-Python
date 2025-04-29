def find_first_and_last(arr, target):
    def binary_search(is_first):
        l, u = 0, len(arr)-1
        result = -1
        while l<= u:
            mid = (l + u) // 2
            if arr[mid] == target:
                result = mid
                if is_first:
                    u = mid -1
                else:
                    l = mid + 1
            elif arr[mid] < target:
                l = mid + 1
            else:
                u = mid - 1
        
        return result
    
    first = binary_search(True)
    last = binary_search(False)
    
    return[first, last]        

arr = [1, 2, 2, 2, 3, 4, 5]
target = 2
print(find_first_and_last(arr, target))