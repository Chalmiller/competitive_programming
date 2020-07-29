from typing import *

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Task: return a list of the matrix as a spiral
        Intuition: It seems like something I could divide and conquer

        Algorithm:
            - traverse the outer shell and return a list
            - peel off the outer shell and place it into the algorithm for another go
            - extend the previous list with the values
        """
        def outer_shell(r1, c1, r2, c2):
            for c in range(c1, c2+1):
                yield r1, c
            for r in range(r1+1, r2+1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2-1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
        
        if not matrix: return []
        ans = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1

        while r1 <= r2 and c1 <= c2:
            for r, c in outer_shell(r1, c1, r2, c2):
                print(r, c)
                ans.append(matrix[r][c])

            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return ans

obj = Solution()
print(obj.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))
