#Uses python3

import sys

def dfs(adj, used, order, x):
    #write your code here
    pass


def toposort(adj):
  """
  Task: Implement topological sort
  Algorithm:
    1. while the adj is non-empty
    2. dfs until the end of the graph
    3. once an end is found, that is the sink, so insert that into a list
    4. remove that vertex from the adj
  """
  used = [0] * len(adj)
  order = []
  #write your code here
  return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

