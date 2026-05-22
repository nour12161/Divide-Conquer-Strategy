import time

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

# Test:
arr = [2, 14, 22, 28, 36, 48, 62, 75, 88, 94]
target = 48

start_time = time.perf_counter()
result = binary_search_iterative(arr, target)
end_time = time.perf_counter()

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")

print("Runtime is:", end_time - start_time, "picosecond")
