import time
def merge_sort_iterative(arr):
    # Split the array into sub-arrays of size 1 and merge them iteratively
    size = 1
    while size < len(arr):
        for start in range(0, len(arr), 2 * size):
            # Calculate mid and end points of the sub-arrays
            mid = start + size - 1
            end = min(start + 2 * size - 1, len(arr) - 1)
            # Merge the sub-arrays
            merge(arr, start, mid, end)
        size *= 2

def merge(arr, start, mid, end):
    # Create temporary arrays to store the sub-arrays
    left = arr[start:mid + 1]
    right = arr[mid + 1:end + 1]

    # Merge the temporary arrays back into arr[start:end+1]
    left_index, right_index, merge_index = 0, 0, start
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[merge_index] = left[left_index]
            left_index += 1
        else:
            arr[merge_index] = right[right_index]
            right_index += 1
        merge_index += 1

    # Add any remaining elements from the left or right sub-array
    while left_index < len(left):
        arr[merge_index] = left[left_index]
        left_index += 1
        merge_index += 1

    while right_index < len(right):
        arr[merge_index] = right[right_index]
        right_index += 1
        merge_index += 1

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
start_time = time.perf_counter()

merge_sort_iterative(arr)
end_time = time.perf_counter()

print("Sorted array:", arr)


print("run time is:",end_time-start_time,"picosecond")
