import collections

class Graph:
  def __init__(self):
    self.graph = collections.defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def dfs_util(self, v, visited):

    visited[v] = True
    print(v, end = " ")
    
    for i in self.graph[v]:
      if visited[i] == False:
        self.dfs_util(i, visited)

  def dfs(self, v):
    visited = [False] * (max(self.graph) + 1)
    self.dfs_util(v, visited)