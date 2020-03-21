from typing import List

def smallerNumbersThanCurrentIterative(nums: List[int]) -> List[int]:
    listCount = []
    for i in nums:
        count = 0
        for j in nums:
            if i > j:
                count += 1
        listCount.append(count)
    return listCount

def smallerNumbersThanCurrentFaster(nums: List[int]) -> List[int]:
    count = {}
    for i, n in enumerate(sorted(nums)):
        print(count)
        if n not in count:
            count[n] = i
            
    return [count[n] for n in nums]

temp_arr = [8,3,2,1,1, 1,1,4,5,2,3,3, 2, 2, 2]
smallerNumbersThanCurrentFaster(temp_arr)