# KOSARAJU algorithm implementation of 
# finding strongly connected components 
# of a directed graph

import unittest
from digraph import DiGraph

class StronglyConnectedComponent:
    def __init__(self, g):
        self.g = g
        self.rg = None
        self.done = [False]*self.g.V
        self.topo_order = []
        self.cc_count = 0
        self.cc_id = [-1]*self.g.V       #Valid id are positive integeres starting from 1
        self.generate_reverse_graph()
        self.populate_topo_order()
        self.populate_strongly_cc()

    def populate_topo_order(self):
        for i in range(self.rg.V):
            if not self.done[i]:
                self.topo_util(i)

    def get_reverse_topo_order(self):
        return list(reversed(self.topo_order))
                
    def topo_util(self, v):
        self.done[v] = True
        for each in self.rg.adj(v):
            if not self.done[each]:
                self.topo_util(each)
        self.topo_order.append(v)
        
    def generate_reverse_graph(self):
        self.rg = DiGraph(self.g.V)
        for i in range(self.rg.V):
            for j in self.g.adj(i):
                self.rg.add_edge(j, i)
    
    def populate_strongly_cc(self):
        self.done = [False]*self.g.V
        for each in self.get_reverse_topo_order():
            if not self.done[each]:
                self.cc_count += 1
                self.cc_dfs(each)

    def cc_dfs(self, v):
        self.done[v] = True
        self.cc_id[v] = self.cc_count
        for each in self.g.adj(v):
            if not self.done[each]:
                self.cc_dfs(each) 

    def get_component_count(self):
        return self.cc_count

    def get_component_id(self, v):
        return self.cc_id[v]    

    def are_strongly_connected(self, v, w):
        return self.get_component_id(v) == self.get_component_id(w)

class TestStronglyConnectedComponent(unittest.TestCase):
    def test_topo_order(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        rto = StronglyConnectedComponent(g).get_reverse_topo_order()
        self.assertListEqual(rto, [4, 5, 1, 0, 3, 2])        

    def test_component_count(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        self.assertEqual(StronglyConnectedComponent(g).get_component_count(), 3)        

    def test_strongly_connected(self):
        g = DiGraph(6)
        g.add_edge(0, 1)
        g.add_edge(0, 2)
        g.add_edge(2, 3)
        g.add_edge(3, 0)
        g.add_edge(2, 4)
        g.add_edge(4, 5)
        g.add_edge(5, 4)
        self.assertTrue(StronglyConnectedComponent(g).are_strongly_connected(0, 2))        
        self.assertTrue(StronglyConnectedComponent(g).are_strongly_connected(3, 2))        
        self.assertTrue(StronglyConnectedComponent(g).are_strongly_connected(4, 5))        
        self.assertFalse(StronglyConnectedComponent(g).are_strongly_connected(4, 2))        


if __name__ == '__main__':
    unittest.main()
