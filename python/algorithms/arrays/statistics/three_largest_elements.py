def find_three_largest(arr, n):
    arr = sorted(arr)

    check = 0
    count = 1

    for i in range(1, n + 1):

        if (count < 4):
            if (check != arr[n - i]):
                print(arr[n - i], end = ' ')
                check = arr[n - i]
                count += 1
        else:
            break
        