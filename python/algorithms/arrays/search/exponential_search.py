def binary_search(arr, key, low, high):
    arr.sort()

    mid = ((low + high) / 2)
    if (arr[mid] == key):
        return mid
    if arr[mid] > key:
        return binary_search(arr, key, mid + 1, high)
    else:
        return binary_search(arr, key, low, mid - 1)

def exponential_search(arr, n, key):
    if arr[0] == key:
        return 0
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2
    return binary_search(arr, key, i/2, min(i, n))
    