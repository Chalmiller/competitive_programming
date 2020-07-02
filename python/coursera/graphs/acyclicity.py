#Uses python3

import sys


def acyclic(adj):
    """
    Algorithm:
      1. find sink and place at end of list
      2. remove sink from graph
      3. repeat
    """
    # Define visited list
    visited = [False] * len(adj)
    rec_cycle = [False] * len(adj)

    # dfs function 
    def dfs(visited, rec_cycle, adj, vertex):
      visited[vertex] = True
      rec_cycle[vertex] = True

      for v in adj[vertex]:
        if not visited[v] and dfs(visited, rec_cycle, adj, v):
          return 1
        if rec_cycle[v]:
          return 1

      rec_cycle[vertex] = False
      return 0
        

    for v in range(len(adj)):
      if not visited[v]:
        if dfs(visited, rec_cycle, adj, v):
          return 1
    
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
