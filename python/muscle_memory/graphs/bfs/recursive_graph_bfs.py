from collections import deque

class Graph:
  
  def __init__(self,  edges, N):
    self.adj_list = [[] for _ in range(N)]

    for (src, dest) in edges:
      self.adj_list[src].append(dest)
      self.adj_list[dest].append(src)

def recursive_bfs(graph, q, discovered):

  if not q:
    return 
  
  v = q.popleft()
  print(v, end = " ")

  for u in graph.adj_list[v]:
    if not discovered[u]:
      discovered[u] = True
      q.append(u)

  recursive_bfs(graph, q, discovered)

def bfs(edges, N):

  graph = Graph(edges, N)
  discovered = [False] * N
  q = deque()

  for i in range(N):
    if not discovered[i]:
      discovered[i] = True
      q.append(i)
      recursive_bfs(graph, q, discovered)