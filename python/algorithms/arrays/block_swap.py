def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp

def leftRotate(arr, d, n):
    if (d == 0 or d == n):
        return
    i = d
    j = n - d
    while ( i != j):
        if (i < j):
            swap(arr, d - i, d + j - i, i)
            j -= i
        else:
            swap(arr, d - i, d, j)
            i -= j
    swap(arr, d - i, d, i)
