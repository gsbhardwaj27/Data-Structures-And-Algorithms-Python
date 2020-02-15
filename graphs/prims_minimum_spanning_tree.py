# Lazy implementation of Prims algorithm
# starts with 0th node
# mark node visited and add adjacent vertices to heap
# delete  smalled edge from heap
# if it has exaxtly one end node in mst add it to mst
# else skip
# repeat above steps untill number of edges in mst is not
# equal to v-1 or heap is not empty

import unittest

from min_heap import MinHeap
from edge_weighted_graph import Edge, EdgeWeightedGraph 


class KruskalsMST:
    def __init__(self, g):
        self.mst = []
        self.g = g
        self.heap = MinHeap()
        self.done = [False]*self.g.V
        self.populate_mst()

    def travel_node(self, node):
        self.done[node] = True
        for each in self.g.adj(node):
            self.heap.add_item(each)

    def populate_mst(self):
        self.travel_node(0)
        while len(self.mst) < self.g.V-1 and not self.heap.is_empty():
            edge = self.heap.del_min()
            if not self.done[edge.either()] and self.done[edge.other(edge.either())]:
                self.travel_node(edge.either())
                self.mst.append(edge)
            elif self.done[edge.either()] and not self.done[edge.other(edge.either())]:
                self.travel_node(edge.other(edge.either()))
                self.mst.append(edge)
                    
    def get_mst(self):
        return self.mst


class TestKruskalsMST(unittest.TestCase):
    def test_mst(self):
        g = EdgeWeightedGraph(8)
        e01 = Edge(0, 1, 2) 
        g.add_edge(e01)
        e02 = Edge(0, 2, 10)
        g.add_edge(e02)
        e16 = Edge(1, 6, 19)
        g.add_edge(e16)
        e13 = Edge(1, 3, 25)
        g.add_edge(e13)
        e24 = Edge(2, 4, 10)
        g.add_edge(e24)
        e27 = Edge(2, 7, 5)
        g.add_edge(e27)
        e23 = Edge(2, 3, 16)
        g.add_edge(e23)
        e36 = Edge(3, 6, 6)
        g.add_edge(e36)
        e35 = Edge(3, 5, 4)
        g.add_edge(e35)
        e47 = Edge(4, 7, 9)
        g.add_edge(e47)
        e45 = Edge(4, 5, 11)
        g.add_edge(e45)
        self.assertListEqual(KruskalsMST(g).get_mst(), [e01, e02, e27, e47, e45, e35, e36])



if __name__ == '__main__':
    unittest.main()
