def merge_sort_recursive(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort_recursive(L)
        merge_sort_recursive(R)

        i, j, k = 0

        while (i < len(L) and j < len(R)):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while (i < len(L)):
            arr[k] = L[i]
            i += 1
            k += 1

        while (j < len(R)):
            arr[k] = R[j]
            j += 1
            k += 1

def merge_sort_iterative(arr):
    current_size = 1

    while current_size < len(arr) - 1:
        left = 0

        while left < len(arr) - 1:
            mid = left + current_size - 1
            right = ((2 * current_size + left - 1, len(arr) - 1)[2 * current_size + left - 1 > len(arr) - 1])
            merge(arr, left, mid, right)
            left = left + current_size * 2
        current_size = 2 * current_size

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m 
    L = [0] * n1 
    R = [0] * n2 
    for i in range(0, n1): 
        L[i] = a[l + i] 
    for i in range(0, n2): 
        R[i] = a[m + i + 1] 
  
    i, j, k = 0, 0, l 
    while i < n1 and j < n2: 
        if L[i] > R[j]: 
            a[k] = R[j] 
            j += 1
        else: 
            a[k] = L[i] 
            i += 1
        k += 1
  
    while i < n1: 
        a[k] = L[i] 
        i += 1
        k += 1
  
    while j < n2: 
        a[k] = R[j] 
        j += 1
        k += 1