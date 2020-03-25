# 1046: Last Stone Weight
from typing import *
import heapq

class Solution:
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     if len(stones) == 1:
    #         return stones[0]
    #     else:
    #         stone_weights = []
    #         first_max = max(stones)
    #         stone_weights.append(stones.pop(stones.index(first_max)))
    #         second_max = max(stones)
    #         stone_weights.append(stones.pop(stones.index(second_max)))
    #         if stone_weights[0] == stone_weights[1]:
    #             stone_weights = []
    #         else:
    #             stone_weights = [abs(stone_weights[0] - stone_weights[1])]
    #         stones.extend(stone_weights)
    #         return self.lastStoneWeight(stones)

        def lastStoneWeight(self, stones: List[int]) -> int:
            q = [-stone for stone in stones]
            heapq.heapify(q)
            while (len(q)) > 1:
                heapq.heappush(q, heapq.heappop(q) - heapq.heappop(q))
            return -q[0]

obj = Solution()
obj.lastStoneWeight([2,7,4,1,8,1])