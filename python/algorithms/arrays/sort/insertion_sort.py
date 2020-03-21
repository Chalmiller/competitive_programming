def insertion_sort_iertative(arr, n):
    i, key, j = 0, 0, 0

    for i in range(n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key

def insertion_sort_recursive(arr, n):
    if n <= 1:
        return
        
    insertion_sort_recursive(arr, n - 1)

    last = arr[n - 1]
    j = n - 2

    while (j >= 0 and arr[j] > last):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = last
