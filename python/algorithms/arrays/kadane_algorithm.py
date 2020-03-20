from sys import maxint

def maxSubArraySum(a, size):
    max_so_far = -maxint - 1
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

def max_sub_array_sum_dynamic(arr, n):
    max_so_far = arr[0]
    curr_max = arr[0]

    for i in range(1, n):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far