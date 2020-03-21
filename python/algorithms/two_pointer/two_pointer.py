def two_pointer(arr, size, target):

    low = 0
    high = size - 1

    while low < high:
        if arr[low] + arr[high] == target:
            return True
        elif arr[low] + arr[high] < target:
            low += 1
        else:
            high += 1
    return False
