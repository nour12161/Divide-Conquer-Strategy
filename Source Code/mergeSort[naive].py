import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    size = 1
    while size < len(arr):
        for start in range(0, len(arr), 2 * size):
            mid = start + size - 1
            end = min(start + 2 * size - 1, len(arr) - 1)
            merge(arr, start, mid, end)
        size *= 2
    
    return arr

def merge(arr, start, mid, end):
    temp = []
    left = start
    right = mid + 1
    
    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1
    
    while left <= mid:
        temp.append(arr[left])
        left += 1
    
    while right <= end:
        temp.append(arr[right])
        right += 1
    
    for i in range(len(temp)):
        arr[start + i] = temp[i]

# TEST:
arr = [38, 27, 43, 3, 9, 82, 10]
start_time = time.perf_counter()

sorted_arr = merge_sort(arr)

end_time = time.perf_counter()
print("Sorted array:", sorted_arr)


print("run time is:",end_time-start_time,"picosecond")
