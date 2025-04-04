def quicksort(arr):
    """
    Sorts a list using the quicksort algorithm.

    Args:
        arr: The list to be sorted.

    Returns:
        A new sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

if __name__ == "__main__":
    # Example usage:
    my_list = [3, 6, 8, 10, 1, 2, 1]
    print("OG list:", my_list)
    sorted_list = quicksort(my_list)
    print("Sorted list:", sorted_list)
