# Depth First Traversal of Graph
# using recursion 
# This limits having longest path eaqual to recursion depth
# Look for dfs with iterative approach using stack

import unittest
from graph import Graph

class DFS:
    def __init__(self, g):
        self.g = g
        self.done = [False for i in range(self.g.V)]
        
    def dfs(self, v):
        data = []
        self.done = [False for i in range(self.g.V)]
        self.dfs_r(v, data)
        return data

    def dfs_r(self, v, data):
        self.done[v] = True
        data.append(v)
        for each in self.g.adj(v):
            if not self.done[each]:
                self.dfs_r(each, data)


class TestDFS(unittest.TestCase):
    def test_dfs(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        self.assertListEqual(DFS(g).dfs(1), [1, 2, 4, 6, 8, 7])
    

if __name__ == '__main__':
    unittest.main()
