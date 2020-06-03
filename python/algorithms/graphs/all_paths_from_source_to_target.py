from typing import *
import collections

class Solution:
  def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    """
    1. generate an adjacency list
    2. dfs search
    3. append path to response list
    3. return response list once all nodes are visited
    """
    paths = []
    path = []
    n = len(graph)

    def dfs(cur):
      nonlocal paths
      nonlocal path
      path.append(cur)

      if cur == n - 1:
        paths.append(path[:])
      else:
        for adj in graph[cur]:
          dfs(adj)
      path.pop()

    dfs(0)
    return paths