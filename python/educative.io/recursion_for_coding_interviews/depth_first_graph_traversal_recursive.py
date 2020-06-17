def helperFunction(myGraph, currentNode, visited) : 
  # Mark the currentNode as visited and print it 
  if(visited[currentNode] == False) :
    visited[currentNode] = True
    print(currentNode) 

  # Recur for all the vertices adjacent to currentNode
  for i in myGraph.graph[currentNode]: 
    if visited[i] == False: 
      helperFunction(myGraph, i, visited) 

def DFS(myGraph): 
  visited = [False]*(myGraph.vertices) # Initially all vertices are marked as unvisited
  helperFunction(myGraph, 0, visited)