from collections import defaultdict

class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def dfs_util(self, v, visited):

    visited[v] = True

    for i in self.graph[v]:
      if not visited[i]:
        self.dfs_util(i, visited)
  
  def dfs(self, v):
    visited = [False] * len(self.graph)

    for node in self.graph:
      # Just in case there are undirected components
      if not visited[node]:
        self.dfs_util(v, visited)

g = Graph() 
g.add_edge(0, 1) 
g.add_edge(0, 2) 
g.add_edge(1, 2) 
g.add_edge(2, 0) 
g.add_edge(2, 3) 
g.add_edge(3, 3) 
  
print("Following is DFS from (starting from vertex 2)") 
g.dfs(2)
