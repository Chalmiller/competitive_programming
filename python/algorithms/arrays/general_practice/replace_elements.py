from typing import *

def replaceElements(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        if i == len(arr) - 1:
            arr[i] = -1
            break
        arr[i] = max(arr[i+1:])
    print(arr)
    return arr

arr = [17,18,5,4,6,1]
replaceElements(arr)
            