from collections import defaultdict, deque()

class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  def add_edge(self, u, v):
    self.graph[u].append(v)

  def dfs(self, s):

    visited = [False] * len(self.graph)
    stack = deque()

    stack.append(s)

    while stack:
      s = stack.pop()
    
      print(s, end=" ")
      visited[s] = True
      for node in self.graph[s]:
        if not visited[node]:
          stack.append(node)

g = Graph(5); # Total 5 vertices in graph  
g.add_edge(1, 0);  
g.add_edge(0, 2);  
g.add_edge(2, 1);  
g.add_edge(0, 3);  
g.add_edge(1, 4);  
  
print("Following is Depth First Traversal")  
g.dfs(0)
