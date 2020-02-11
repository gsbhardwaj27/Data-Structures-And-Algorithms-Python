# Find longest path in Graph
# Graph does not have cycles

import unittest
from graph import Graph

class GraphCenter:
    def __init__(self, g):
        self.g = g
        self.done = [False]*self.g.V
        self.dist = [0]*self.g.V
        
    def get_center(self):
        for i in range(self.g.V):
            self.done = [False]*self.g.V
            self.calculate_dist_sum(i, i, 0)
        return self.dist.index(min(self.dist))
            
    
    def calculate_dist_sum(self, v, start, curr_dist):
        self.done[v] = True
        self.dist[start] += curr_dist
        for each in self.g.adj(v):
            if not self.done[each]:
                self.calculate_dist_sum(each, start, curr_dist+1) 

class TestGraphCenter(unittest.TestCase):
    def test_1(self):
        g = Graph(3)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        self.assertTrue(GraphCenter(g).get_center(), 1)        

    def test_2(self):
        g = Graph(7)
        g.add_edge(0, 2)
        g.add_edge(1, 2)
        g.add_edge(2, 3)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(6, 5)
        self.assertTrue(GraphCenter(g).get_center(), 2)        
    

if __name__ == '__main__':
    unittest.main()
