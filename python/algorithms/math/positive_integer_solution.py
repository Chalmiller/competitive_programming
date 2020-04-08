# 1237: Find Positive Integer Solution for a Given Equation
from typing import *

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        for i in range(z):
            for j in range(z):
                if 