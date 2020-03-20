def bubble_sort_iterative(array):
    arr_length = len(array)
    for i in range(arr_length):
        for j in range(0, arr_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def bubble_sort_recursive(arr):
    for i, num in enumerate(arr):
        try:
            if arr[i + 1] < num:
                arr[i] = arr[i + 1]
                arr[i + 1] = num
                bubble_sort_recursive(arr)
        except indexError:
            pass
    return arr

test_array = [5,2,6,3,4567,54,23,6,1]

bubble_sort(test_array)
