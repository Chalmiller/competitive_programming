from typing import *

def findDisappearedNumbers(nums: List[int]) -> List[int]:
    num_set = set(nums)
    n_set = set(range(1, len(nums)+1))
    return(list(n_set.difference(num_set)))

numbers = [4,3,2,7,8,2,3,1]
findDisappearedNumbers(numbers)
