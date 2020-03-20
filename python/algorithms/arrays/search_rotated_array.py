def binary_search(arr, low, high, key):
    if high < low:
        return -1
    mid = int((low + high)/2)

    if key == arr[mid]:
        return mid
    if key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)
    else:
        return binary_search(arr, low, mid - 1, key)

def pivotedBinarySearch(arr, n, key):
    pivot = findPivot(arr, 0, n - 1)

    if (pivot == -1):
        return binary_search(arr, 0, n - 1, key)

    if arr[pivot] == key:
        return pivot
    if arr[0] < key:
        return binary_search(arr, 0, pivot - 1, key)
    else:
        return binary_search(arr, pivot + 1, n - 1, key)

def findPivot(arr, low, high):
    if high < low:
        return -1
    if high == low:
        return low

    mid = int((low + high)/2)

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid - 1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid - 1)
    return findPivot(arr, mid + 1, high)

    