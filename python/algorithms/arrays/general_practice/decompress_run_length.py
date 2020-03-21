from typing import *

def decompressRLElist(nums: List[int]) -> List[int]:
    cache = []
    for i in range(len(nums)//2):
        temp_list = [nums[2*i], nums[2*i+1]]
        cache.append([temp_list[1]]*temp_list[0])
    flat_cache = [item for sublist in cache for item in sublist]
    return flat_cache

nums = [1,2,3,4]
decompressRLElist(nums)
