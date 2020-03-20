def swap(array, index1, index2):
    temp = array[index1]
    array[index1] = array[index2]
    array[index2] = temp

def insertion_sort(array):
    arr_length = len(array)

    for i in range(arr_length):
        min_val = i
        for j in range(i+1, arr_length):
            if array[min_val] > array[j]:
                min_val = j
        
        if (min_val != i):
            swap(array, i, min_val)
    print(array)
    return array

test_array = [5,2,6,3,4567,54,23,6,1]
insertion_sort(test_array)