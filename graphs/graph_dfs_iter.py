# Iterative way of Depth first graph traversal
# limited only by system  memory

import unittest
from graph import Graph

class DFS:
    def __init__(self, g):
        self.g = g
        
    def dfs(self, v):
        data = []
        stack = [v]
        done = [False for i in range(self.g.V)]
        while stack:
            node = stack.pop()
            data.append(node)
            done[node] = True
            for each in self.g.adj(node):
                if not done[each]:
                    stack.append(each)
        return data


class TestDFS(unittest.TestCase):
    def test_dfs(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        self.assertListEqual(DFS(g).dfs(1), [1, 8, 7, 2, 6, 4])
    

if __name__ == '__main__':
    unittest.main()
