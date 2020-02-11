# Find longest path in Graph
# Graph does not have cycles

import unittest
from graph import Graph

class LongestPath:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
        self.longest_path = []
        
    def get_longest_path(self):
        stack = [0]
        done = [False]*self.g.V
        node = None
        while stack:
            node = stack.pop()
            done[node] = True
            for each in self.g.adj(node):
                if not done[each]:
                     stack.append(each)
        # We should endup at either end of node which is
        # part of longest path
        end_node = node
        self.find_longest_path(end_node, [])
        return self.longest_path
        # Now lets start with this end node and count 

    
    def find_longest_path(self, v, path):
        path.append(v)
        self.done[v] = True
        if len(path) > len(self.longest_path):
            self.longest_path = list(path)
        for each in self.g.adj(v):
            if not self.done[each]:
                self.find_longest_path(each, path)
        path.pop()
 

class TestLongestPath(unittest.TestCase):
    def test_1(self):
        g = Graph(2)
        g.add_edge(0, 1)
        self.assertEqual(len(LongestPath(g).get_longest_path()), 2)        
        self.assertListEqual(LongestPath(g).get_longest_path(), [1, 0])        

    def test_2(self):
        g = Graph(7)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(6, 5)
        self.assertEqual(len(LongestPath(g).get_longest_path()), 5)        
        self.assertEqual(LongestPath(g).get_longest_path(), [1, 2, 4, 5, 6])        
    

if __name__ == '__main__':
    unittest.main()
