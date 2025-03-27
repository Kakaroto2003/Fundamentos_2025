def linear_search(array, target):
    """Performs linear search on the array for the target element.

    Args:
        array (list): list of elements to search through.
        target (integer): element to search for.

    Returns:
        integer: index of the target element in the array. -1 if not found.
    """
    for index in range(len(array)):
        if array[index] == target:
            return index
    return -1

# Example
array = [10, 23, 45, 70, 11, 15]
target = 70

result = linear_search(array, target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found in the array")