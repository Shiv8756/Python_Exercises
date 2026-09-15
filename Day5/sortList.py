def sort_with_loops(arr):
    n = len(arr)

    # Outer loop for the number of passes
    for i in range(n):
        # Inner loop compares adjacent elements
        # The last 'i' elements are already in place, so we subtract 'i'
        for j in range(0, n - i - 1):

            # If the current element is greater than the next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


# Test the function
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = sort_with_loops(numbers)

print("Sorted list:", sorted_numbers)