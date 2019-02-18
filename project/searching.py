# STRETCH: implement Linear Search
def linear_search(arr, target):
    for indx, num in enumerate(arr):
        if num == target:
            return(indx)

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1

    # TO-DO: add missing code

    return -1  # not found


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target):

    middle = len(arr)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls
    else:
        if target == arr[middle]:
            return target
        elif target < arr[middle]:
            binary_search_recursive(arr[:middle], target)
        elif target > arr[middle]:
            binary_search_recursive(arr[middle:], target)

    return arr.index(target)
