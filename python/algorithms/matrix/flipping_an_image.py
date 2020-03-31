# 832: Flipping an Image
from typing import *

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped_list = [row[::-1] for row in A]
        for index in range(len(flipped_list)):
            for num in range(len(flipped_list[index])):
                if flipped_list[index][num] == 0:
                    flipped_list[index][num] = 1
                else:
                    flipped_list[index][num] = 0
        return flipped_list

obj = Solution()
num = obj.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]])
print(num)
