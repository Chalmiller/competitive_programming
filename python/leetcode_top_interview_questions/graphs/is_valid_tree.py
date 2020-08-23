from collections import defaultdict, deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False

        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        visited = set()
        queue = deque([0])
        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node in visited: 
                    continue
                visited.add(node)
                for child in graph[node]: 
                    queue.append(child)
        return len(visited) == n
