import time

def naive_binary_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1  # Target not found

# Test data
arr = [2, 14, 22, 28, 36, 48, 62, 75, 88, 94]
target = 48

start_time = time.perf_counter()
result = naive_binary_search(arr, target)
end_time = time.perf_counter()

elapsed_time_seconds = end_time - start_time

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found in the array.")

print("Runtime is:", elapsed_time_seconds, "picosecond")
