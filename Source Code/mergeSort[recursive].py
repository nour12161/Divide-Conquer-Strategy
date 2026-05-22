import time

def merge_sort_recursive(arr):
    if len(arr) <= 1:
        return

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    merge_sort_recursive(left_half)
    merge_sort_recursive(right_half)

    # Merge the sorted halves
    merge(arr, left_half, right_half)

def merge(arr, left, right):
    left_index = 0
    right_index = 0
    merge_index = 0

    # Merge the elements from left and right arrays into arr
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            arr[merge_index] = left[left_index]
            left_index += 1
        else:
            arr[merge_index] = right[right_index]
            right_index += 1
        merge_index += 1

    # Add any remaining elements from left or right arrays
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

merge_sort_recursive(arr)

end_time = time.perf_counter()

print("Sorted array:", arr)
print("Runtime is:", end_time - start_time, "picosecond")
