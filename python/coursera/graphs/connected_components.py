#Uses python3
import sys

def number_of_components(adj):
    visited = [False] * len(adj)

    def dfs(visited, adj, vertex):
      visited[vertex] = True
      for v in adj[vertex]:
        if not visited[v]:
          dfs(visited, adj, v)

    count = 0
    for v in range(len(adj)):
      if not visited[v]:
        dfs(visited, adj, v)
        count += 1

    return count

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
