import unittest
from edge_weighted_graph import Edge, EdgeWeightedGraph
from indexed_heap import MinIndexedHeap 


class Dijkstra:
    def __init__(self, g, start):
        self.g = g
        self.minheap = MinIndexedHeap([float("inf")]*g.V)
        self.done = [False]*self.g.V
        self.dist = [float("inf")]*self.g.V
        self.prev = [None]*self.g.V
        self.relex_edges(start)
        

    def relex_edges(self, curr):
        # start vertex distanc is 0
        self.minheap.decrease_key(curr, 0)
        self.dist[curr] = 0
        for i in range(self.g.V-1):
            weight, curr = self.minheap.del_min()
            self.dist[curr] = weight
            self.done[curr] = True
            for edge in self.g.adj(curr):
                w = edge.other(edge.either())
                if not self.done[w] and self.dist[w] > (self.dist[curr] + edge.wt):
                    self.dist[w] = self.dist[curr] + edge.wt
                    self.prev[w] = curr
                    self.minheap.decrease_key(w, self.dist[w])

    def get_path(self, w):
        path = []
        i = w
        while i is not None:
            path.append(i)
            i = self.prev[i]
        return list(reversed(path))


class TestDijkstra(unittest.TestCase):
    def test_path(self):
        g = EdgeWeightedGraph(4)
        e1 = Edge(0, 1, 2)
        e2 = Edge(0, 2, 5)
        e3 = Edge(1, 3, 10)
        e4 = Edge(2, 3, 3)
        g.add_edge(e1)
        g.add_edge(e2)
        g.add_edge(e3)
        g.add_edge(e4)
        self.assertListEqual(Dijkstra(g, 0).get_path(3), [0, 2, 3])


if __name__ == '__main__':
    unittest.main()
