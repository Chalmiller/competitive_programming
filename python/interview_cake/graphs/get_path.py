import unittest
from collections import deque


def get_path(graph, start_node, end_node):

    """
    Task: Find the shortest routing from one person to another
    Intuition: This is a direct use case of DFS

    Algorithm:
      - iterate through the adjacency list using dfs
      - once the endpoint is reached, return the path
    """

    def reconstruct_path(previous_nodes, start_node, end_node):
      reversed_shortest_path = []
      current_node = end_node

      while current_node:
        reversed_shortest_path.append(current_node)
        current_node = previous_nodes[current_node]

      reversed_shortest_path.reverse()
      return reversed_shortest_path

    if start_node not in graph:
      raise Exception('Start node not in graph')
    if end_node not in graph:
      raise Exception('End node not in graph')

    shortest_path = []

    # Using a set instead of a falsey list
    seen = set()

    stack = deque()
    stack.append(start_node)

    how_we_reached_nodes = {start_node: None}

    while stack:
      cur_el = stack.popleft()
      shortest_path.append(cur_el)

      if cur_el == end_node:
        return reconstruct_path(how_we_reached_nodes, start_node, end_node)

      for node in graph[cur_el]:
        if node not in seen:
          stack.append(node)
          seen.add(node)
    return None


# Tests
class Test(unittest.TestCase):

    def setUp(self):
        self.graph = {
            'a': ['b', 'c', 'd'],
            'b': ['a', 'd'],
            'c': ['a', 'e'],
            'd': ['a', 'b'],
            'e': ['c'],
            'f': ['g'],
            'g': ['f'],
        }

    def test_two_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'e')
        expected = ['a', 'c', 'e']
        self.assertEqual(actual, expected)

    def test_two_hop_path_2(self):
        actual = get_path(self.graph, 'd', 'c')
        expected = ['d', 'a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_1(self):
        actual = get_path(self.graph, 'a', 'c')
        expected = ['a', 'c']
        self.assertEqual(actual, expected)

    def test_one_hop_path_2(self):
        actual = get_path(self.graph, 'f', 'g')
        expected = ['f', 'g']
        self.assertEqual(actual, expected)

    def test_one_hop_path_3(self):
        actual = get_path(self.graph, 'g', 'f')
        expected = ['g', 'f']
        self.assertEqual(actual, expected)

    def test_zero_hop_path(self):
        actual = get_path(self.graph, 'a', 'a')
        expected = ['a']
        self.assertEqual(actual, expected)

    def test_no_path(self):
        actual = get_path(self.graph, 'a', 'f')
        expected = None
        self.assertEqual(actual, expected)

    def test_start_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'h', 'a')

    def test_end_node_not_present(self):
        with self.assertRaises(Exception):
            get_path(self.graph, 'a', 'h')


unittest.main(verbosity=2)