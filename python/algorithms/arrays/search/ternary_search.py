def ternary_search(arr, key, low, high):
    if (high >= low):
        mid1 = low + (high - low)/3
        mid2 = high - (high - low)/3

        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        
        if (key < arr[mid1]):
            return ternary_search(arr, key, low, mid1 - 1)
        elif (key > arr[mid2]):
            return ternary_search(arr, key, mid2 + 1, high)
        else:
            return ternary_search(arr, key, mid1 + 1, mid2 - 1)
    return -1