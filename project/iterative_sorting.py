# Complete the selection_sort() function below in class with your instructor
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
            print(f'smallest element: {arr[smallest_index]}')

            # swamp
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp
            # arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):
        cur_index = arr[i]

        while i > 0 and arr[i-1] > cur_index:
            arr[i] = arr[i - 1]
            i -= 1
            arr[i] = cur_index

    return arr


# STRETCH: implement the Bubble Sort function below
def bubble_sort(arr):
    is_sorted = False

    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i +1]:
                arr[i], arr[i +1] = arr[i+1], arr[i]
                is_sorted = False
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
