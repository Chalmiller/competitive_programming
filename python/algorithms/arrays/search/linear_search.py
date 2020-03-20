def linear_search(arr, key):

    for i, el in enumerate(arr):
        if el == key:
            return i
    return -1