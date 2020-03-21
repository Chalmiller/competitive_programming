def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)

def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n-1):
        arr[i] = arr[i + 1]
        print(arr)
    arr[n - 1] = temp

arr = [1, 2, 3, 4, 5, 6, 7] 
leftRotate(arr, 2, 7) 