from typing import *
import unittest
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Task: Order the courses needed to graduate, or whatever
        Intuition: I in fact know this is topological sort.
        
        Algorithm: 
            - build indegree hashmap for each parent vertex
            - find the source node and run bfs on the graph from there
            - each time a node is popped, subtract the indegree of the children of it
        """

        in_degree = {i: 0 for i in range(numCourses - 1)}
        graph = {i: [] for i in range(numCourses - 1)}
        visited = [False] * numCourses

        topological_order = []
        queue = deque()

        for child, parent in prerequisites:
            in_degree[child] += 1
            graph[parent].append(child)

        for node in graph.keys():
            if in_degree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            if visited[node]:
                return False
            else:
                visited[node] = True
                topological_order.append(node)
                for child in graph[node]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        queue.append(child)
        return True

class TestCanFinish(unittest.TestCase):
    
    def test_can_finish(self):
        pass

unittest.main(verbosity=2)
