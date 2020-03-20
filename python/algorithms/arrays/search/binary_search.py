def binary_search(arr, key, low, high):
    arr.sort()

    mid = ((low + high) / 2)
    if (arr[mid] == key):
        return mid
    if arr[mid] > key:
        return binary_search(arr, key, mid + 1, high)
    else:
        return binary_search(arr, key, low, mid - 1)