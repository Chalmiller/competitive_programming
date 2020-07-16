from collections import defaultdict, deque

class Graph:

  def __init__(self):
    self.graph = defaultdict(list)
  
  def addEdge(self,u, v):
    self.graph[u].append(v)

  def bfs(self, s):

    visited = [False] * len(self.graph)

    queue = deque()
    queue.append(s)
    visited[s] = True

    while queue:
      s = queue.popleft()
      print(s, end=" ")

      for i in self.graph[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True

