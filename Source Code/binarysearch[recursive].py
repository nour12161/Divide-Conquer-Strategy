import time

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

# Test:
arr = [2, 14, 22, 28, 36, 48, 62, 75, 88, 94]
target = 48
start_time = time.perf_counter()

result = binary_search_recursive(arr, target, 0, len(arr) - 1)

end_time = time.perf_counter()

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")

print("run time is:",end_time - start_time, "picosecond")
