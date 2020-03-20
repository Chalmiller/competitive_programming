def interpolation_search(arr, n, key):
    lo = 0
    hi = (n - 1)

    while (lo <= hi and key >= arr[lo] and key <= arr[hi]):
        if lo == hi:
            if arr[lo] == key:
                return lo
            return -1

        pos = lo + int((float(hi - lo / (arr[hi] - arr[lo])) * (key - arr[lo])))

        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            lo = pos + 1
        else:
            hi = pos - 1

    return -1