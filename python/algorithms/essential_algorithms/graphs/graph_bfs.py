import collections

class Graph:
  def __init__(self):
    self.graph = collections.defaultdict(list)

  def addEdge(self, u, v):
    self.graph[u].append(v)

  def bfs(self, s):
    visited = [False] * (len(self.graph))

    queue = []

    queue.append(s)
    visited[s] = True

    while queue:
      s = queue.pop(0)

      for i in self.graph[s]:
        if visited[i] == False:
          queue.append(i)
          visited[i] = True