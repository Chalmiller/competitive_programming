from random import randint
def randomPartition(arr, l, r):
    n = r - l + 1
    pivot = randint(1, 100) % n
    arr[l + pivot], arr[r] = arr[l + pivot], arr[r]
    return partition(arr, l, r)

def kthSmallest(arr, l, r, k):
    if ( k > 0 and k <= r - l + 1):
        pos = randomPartition(arr, l, r)

        if (pos - 1 == k - 1):
            return arr[pos]

        if (pos - l > k - 1):
            return kthSmallest(arr, l, pos - 1, k)

        return kthSmallest(arr, pos + 1, r, k - pos + l - 1)
    return 10**9

def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[j], arr[r] = arr[r], arr[i]
    return i
