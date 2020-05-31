from typing import *

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            diag = [mat[i+j][j] for j in range(min(m-i, n))]
            print(diag)
            diag.sort()
            for j in range(min(m-i, n)):
                mat[i+j][j] = diag[j]
            print(mat)

        for j in range(1,n):
            diag = [mat[i][j+i] for i in range(min(n-j, m))]
            print(diag)
            diag.sort()
            for i in range(min(n-j, m)):
                mat[i][j+i] = diag[i]
        return mat
          
obj = Solution()
print(obj.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]]))
            