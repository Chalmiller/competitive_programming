from typing import *
import unittest
from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Task: Count the total number of connected components
        Intuition: Union find to return the total visited nodes 

        Algorithm: 
            - generate a recursive algorithm which traverses the components of a graph and populates a visited_table
            - after each iteration of the recursive function, increment the counter
        """
        adj_list = defaultdict(list)
        visited = [False] * n

        if not edges:
            return n

        for v, e in edges:
            adj_list[v].append(e)
            adj_list[e].append(v)

        num_components = 0

        for node in range(n):
            if not visited[node]:
                num_components += 1
                self.dfs(node, adj_list, visited)

        return num_components
    
    def dfs(self, node, graph, visited):
        visited[node] = True

        for edge in graph[node]:
            if not visited[edge]:
                self.dfs(edge, graph, visited)
        return
        

class TestConnectedComponents(unittest.TestCase):
    def test_count_components(self):
        pass

unittest.main(verbosity=2)
