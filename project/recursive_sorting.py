# helper function
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    a = 0
    b = 0
    # since arrA and arrB already sorted, we only need to compare the first element of each when merging!
    for i in range(0, elements):
        if a >= len(arrA):    # all elements in arrA have been merged
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):  # all elements in arrB have been merged
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:  # next element in arrA smaller, so add to final array
            merged_arr[i] = arrA[a]
            a += 1
        else:  # else, next element in arrB must be smaller, so add it to final array
            merged_arr[i] = arrB[b]
            b += 1
    return merged_arr


# recursive sorting function
def merge_sort(arr):
    if len(arr) > 1:
        left = merge_sort(arr[0: len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)   # merge() defined later
    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# TO-DO: implement the Quick Sort function below USING RECURSION
def quick_sort(arr, low, high):

    pivot = low
    count = low

    if low < high:
        for i in range(low + 1, high + 1):
            if arr[i] < arr[pivot]:
                count += 1
                a = arr[i]
                b = arr[count]
                arr[i], arr[count] = b, a

        x = arr[count]
        y = arr[pivot]
        arr[count], arr[pivot] = y, x

        quick_sort(arr, low, count - 1)
        quick_sort(arr, count + 1, high)
    return arr


arr3 = [10, 1, 13, 3, 2, 6, 5, 25]

print(quick_sort(arr3, 0, len(arr3)-1))


def quick_sort_high(arr, low, high):

    pivot = high
    count = low

    if low < high:
        for i in range(low, high):
            if arr[i] < arr[pivot]:
                a = arr[i]
                b = arr[count]
                arr[i], arr[count] = b, a
                count += 1

        x = arr[pivot]
        y = arr[count]
        arr[pivot], arr[count] = y, x

        quick_sort_high(arr, low, count - 1)
        quick_sort_high(arr, count + 1, high)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt


def timsort(arr):

    return arr
