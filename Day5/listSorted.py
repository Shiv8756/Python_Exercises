def is_list_sorted(lst):
    # Check if every element is <= the next element
    return list(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(is_list_sorted([10, 20, 30, 25, 40]))