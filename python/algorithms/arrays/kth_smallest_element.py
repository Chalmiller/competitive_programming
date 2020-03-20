def kth_smallest_element(arr, k):
    arr.sort()
    return arr[k - 1]