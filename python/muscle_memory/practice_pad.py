from collections import defaultdict


"""
This practice pad will serve as the daily msucle memory practice of the most common algorithms
I will need to solve questions from the following categories:
  1. Graphs
    - bfs
    - dfs
      - iterative
      - recursive
    - topological sort
    - connected components
    - minimum spanning tree
    - shortest path 
  2. Trees
    - bfs
    - dfs
      - iterative
      - recursive
  3. Search
    - binary search
    - quick select
  4. Sort
    - quick sort (for small arrays)
    - merge sort (for large arrays)
  5. Dynamic Programming
  6. Linked Lists
  7. Greedy Algorithms
  8. Divide and Conquer

"""
# Tree Node
class node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

class Graph:

  def __init__(self):
    self.graph = defaultdict(list)

  # u is a vertex and v is an edge
  def add_edge(self, u, v):
    self.graph[u].append(v)

# Tree Traversal

# Graph Traversal

# Searching 

# Sorting
  
