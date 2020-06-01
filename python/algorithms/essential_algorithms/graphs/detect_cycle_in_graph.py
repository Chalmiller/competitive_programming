from collections import defaultdict

class Graph:
  def __init__(self, vertices):
    self.graph = defaultdict(list)
    self.V = vertices

  def addEdge(self,u, v):
    self.graph[u].append(v)

  def isCyclicUtil(self, v, visited, recStack):
    visited[v] = True
    recStack[v] = True

    for neighbor in self.graph[v]:
      if visited[neighbor] == False:
        if self.isCyclicUtil(neighbor, visited, recStack) == True:
          return True
        elif recStack[neighbor] == True:
          return True
    recStack[v] = False
    return False

  def isCyclic(self):
    visited = [False] * self.V
    recStack = [False] * self.V
    for node in range(self.V):
      if visited[node] == False:
        if self.isCyclicUtil(node, visited, recStack) == True:
          return True
    return False