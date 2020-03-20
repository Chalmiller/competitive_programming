def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def bubble_sort(array):
    arr_length = len(array)
    for i in range(arr_length):
        for j in range(arr_length):
            if array[i] < array[j]:
                swap(array, i, j)
                print(array)
    return array

test_array = [5,2,6,3,4567,54,23,6,1]

bubble_sort(test_array)
