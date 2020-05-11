from collections import defaultdict
from typing import *

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        print(graph)

        has_subtree = hasApple[:]
        print(has_subtree)

        def dfs(node, par = -1):
          for nei in graph[node]:
            if nei != par:
              dfs(nei, node)
              if has_subtree[nei]:
                print("nei: {}".format(nei), "is_subtree: {}".format(has_subtree[nei]))
                self.ans += 2
                has_subtree[node] = True
                print("node: {}".format(node), "is_now_subtree: {}".format(has_subtree[node]))
          print("has_subtree at the end {}".format(has_subtree))
                

        self.ans = 0
        dfs(0)
        return self.ans

        

obj = Solution()
print(obj.minTime(7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], [False,False,True,False,True,True,False]))