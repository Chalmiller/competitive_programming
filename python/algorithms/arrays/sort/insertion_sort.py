def insertion_sort(arr, n):
    i, key, j = 0, 0, 0

    for i in range(n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
