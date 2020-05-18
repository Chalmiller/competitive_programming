from typing import *
import collections

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        if len(time) ==0:
            return 0
        
        remain = collections.defaultdict(list)
        print(list(remain))
        count = 0
        
        for t in time:
            key = t % 60
            print(t,key)
            com_key = (60 - key) % 60 # Complementary key
            print(com_key)
            
            if com_key in remain:
                count += len(remain[com_key]) # because the elements in complementary list must have smaller indices, so we can count all of them
                
            remain[key].append(t)
            print(remain, count)
            
        return count

obj = Solution()
print(obj.numPairsDivisibleBy60([30,20,150,100,40]))