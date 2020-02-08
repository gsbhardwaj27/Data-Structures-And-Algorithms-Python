# Connected components using grapth traversal
# Here i am using depth first graph traversal

import unittest

from graph import Graph


class ConnectedComponents:
    def __init__(self, g):
        self.g = g
        self.comp = [-1 for x in range(self.g.V)]
        self.comp_count = 0
    
        for node in range(self.g.V):
            if self.comp[node] == -1:
                self.comp_count += 1
                self.dfs(node)
                
    def dfs(self, node):
        self.comp[node] = self.comp_count
        for each in self.g.adj(node):
            if self.comp[each] == -1:
                self.dfs(each)       
    
    
    def is_connected(self, v, w):
        return self.comp[v] == self.comp[w]

    def count(self):
        return self.comp_count


class TestConnectedComponents(unittest.TestCase):
    def test_cc(self):
        g = Graph(8)
        g.add_edge(0, 1)
        g.add_edge(0, 5)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(6, 7)
       
        cc = ConnectedComponents(g)
        self.assertFalse(cc.is_connected(0, 4)) 
        self.assertTrue(cc.is_connected(0, 3)) 
        self.assertFalse(cc.is_connected(2, 7)) 
        self.assertFalse(cc.is_connected(4, 7)) 
        self.assertTrue(cc.is_connected(6, 7)) 


    def test_comp_count(self):
        g = Graph(8)
        g.add_edge(0, 1)
        g.add_edge(0, 5)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(6, 7)
       
        cc = ConnectedComponents(g)
        self.assertTrue(cc.count()==3) 
        

if __name__ == '__main__':
    unittest.main()
