def linear_search(arr, key):

    for i, el in enumerate(arr):
        if el == key:
            return i
    return -1

def recursive_search(arr, low, high, key):
    if high < low:
        return -1
    if arr[low] == key:
        return low
    if arr[high] == key:
        return high
    return recursive_search(arr, low + 1, high - 1, key)