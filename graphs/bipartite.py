# Bipartite graph 
# For an example we will have two types of nodes
# one which are even numbered and other which are odd nubered
# 0 will be even
import unittest
from graph import Graph
from collections import deque

class Bipartite:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V

    def is_bipartite(self):
        for i in range(self.g.V):
           if not self.done[i]:
                self.done[i] = True
                if not self.bfs(i):
                    return False
        return True 

    def bfs(self, node):
        q = deque()
        q.append(node)
        while q:
            node = q.popleft()
            self.done[node] = True
            for each in self.g.adj(node):
                if not self.done[each]:
                    if self.node_type(each) == self.node_type(node):
                        return False
                    else:
                        q.append(each)
                
        return True

    def node_type(self, v):
        # This can be based on any complex structure also
        # we are taking this and an exmple
        return 1 if v%2==0 else 2      
        
            
class TestGraphBP(unittest.TestCase):
    def test_notbp(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        self.assertFalse(Bipartite(g).is_bipartite())

    def test_bp(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(5, 6)
        g.add_edge(3, 8)
        g.add_edge(1, 8)
        self.assertTrue(Bipartite(g).is_bipartite())

if __name__ == '__main__':
    unittest.main()
