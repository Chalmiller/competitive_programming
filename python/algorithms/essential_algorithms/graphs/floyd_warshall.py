import math

vertices = 4
def floydWarshall(graph):
  dist = map(lambda i: map(lambda j: j, i), graph)

  for k in range(vertices):
    for i in range(vertices):
      for j in range(vertices):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

  printSolution(dist)

def printSolution(dist):
  print("Following matrix shows the shortest distances between every pair of vertices")

  for i in range(vertices):
    for j in range(vertices):
      if (dist[i][j] == math.inf):
        print(math.inf)
      else:
        print("%7d\t" %(dist[i][j]))
      if j == vertices-1:
        print()
