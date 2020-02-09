# Find eularian path in a graph

import unittest
from graph import Graph
from collections import deque

class EulerianPath:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
        self.odd_degree_nodes = []        
        self.path = []
        self.find_path()

    def dfs(self, v):
        self.done[v] = True

        if len(self.g.adj(v)) % 2 == 1:
            self.odd_degree_nodes.append(v)

        for each in self.g.adj(v):
            if not self.done[each]:
                self.dfs(each)
        
    def has_path(self):
        # Graph must be connected
        # There should  be 0 or 2 nodes with odd degrees
        self.dfs(0) #Can be any node, picked 0
        if False in self.done or len(self.odd_degree_nodes) not in(0, 2):
            return False
        else:
            return True
        
        
    def find_path(self):
        if not self.has_path():
            return []
        stack = []
        curr = self.odd_degree_nodes[0] if self.odd_degree_nodes else 0
        stack.append(curr)
        while stack:
            curr = stack[-1]
            if self.g.adj(curr):
                tmp = self.g.adj(curr)[-1]
                # delete this edge
                self.g.adj(curr).remove(tmp)
                self.g.adj(tmp).remove(curr)
                stack.append(tmp)
            else:
                self.path.append(curr)
                stack.pop()
        
    def get_path(self):
        return self.path
    

class TestEulerianPath(unittest.TestCase):
    def test_no_path(self):
        g = Graph(3)
        g.add_edge(1, 2)
        self.assertListEqual(EulerianPath(g).get_path(), [])

    def test_no_path(self):
        g = Graph(3)
        g.add_edge(1, 0)
        g.add_edge(1, 2)
        g.add_edge(0, 2)
        self.assertListEqual(EulerianPath(g).get_path(), [0, 1, 2, 0])

    def test_no_path(self):
        g = Graph(3)
        g.add_edge(1, 0)
        g.add_edge(1, 2)
        self.assertListEqual(EulerianPath(g).get_path(), [2, 1, 0])

    def test_no_path(self):
        g = Graph(6)
        g.add_edge(1, 0)
        g.add_edge(1, 0)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 3)
        g.add_edge(4, 3)
        g.add_edge(4, 3)
        # print(EulerianPath(g).get_path())
        self.assertListEqual(EulerianPath(g).get_path(), [0, 1, 2, 4, 5, 3, 4, 3, 1, 0])

    def test_no_path(self):
        g = Graph(7)
        g.add_edge(1, 0)
        g.add_edge(6, 3)
        g.add_edge(1, 3)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 3)
        g.add_edge(4, 3)
        g.add_edge(4, 3)
        self.assertListEqual(EulerianPath(g).get_path(), [6, 3, 1, 2, 4, 5, 3, 4, 3, 1, 0])

if __name__ == '__main__':
    unittest.main()
