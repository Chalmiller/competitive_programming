def dfs(graph, vertex, discovered):
  for e in graph.incident_edges(vertex):
    v = e.opposite(u)
    if v not in discovered:
      discovered[v] = e
      dfs(graph, v, discovered)