# STRETCH: implement Linear Search
def linear_search(arr, target):
    for num in arr:
        if num == target:
            return arr.index(num)

    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):

    mid = len(arr)//2
    low = 0
    high = len(arr)-1

    if len(arr) == 0:
        return -1  # array empty

    elif target == arr[mid]:
        return arr.index(target)
    elif target < arr[mid]:
        for i in range(low, arr[mid]):
            if arr[i] == target:
                return arr.index(target)
    elif target > arr[mid]:
        for i in range(arr[mid], high + 1):
            if arr[i] == target:
                return arr.index(target)

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
