# Breadth First Traversal of Graph
# Limited by memory available
# complexity

import unittest
from graph import Graph
from collections import deque

class HasCycle:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
        self.curr = [False]*self.g.V
        self.has_cycle = False
        self.look_for_cycle()

    def dfs(self, v, prev=None):
        self.curr[v] = True #For each component
        self.done[v] = True
        for each in self.g.adj(v):
            if self.curr[each] and each != prev:
                self.has_cycle = True
                return
            elif not self.curr[each]:
                self.dfs(each, v)
        
    def look_for_cycle(self):
        for i in range(self.g.V):
            if not self.done[i]:
                self.curr = [False]*self.g.V
                self.dfs(i)
                if self.has_cycle:
                    return
        
    def graph_has_cycle(self):
        return self.has_cycle


class TestBFS(unittest.TestCase):
    def test_no_cycle(self):
        g = Graph(3)
        g.add_edge(1, 2)
        self.assertFalse(HasCycle(g).graph_has_cycle())

    def test_no_cycle_1(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        self.assertFalse(HasCycle(g).graph_has_cycle())

    def test_have_cycle(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(1, 3)
        g.add_edge(2, 4)
        g.add_edge(3, 4)
        g.add_edge(1, 8)
        self.assertTrue(HasCycle(g).graph_has_cycle())
    

if __name__ == '__main__':
    unittest.main()
