import unittest
from edge_weighted_graph import Edge, EdgeWeightedGraph
from indexed_heap import MinIndexedHeap


class BellmanFord:
    def __init__(self, g, start):
        self.g = g
        self.dist = [float("inf")]*self.g.V
        self.prev = [None]*self.g.V
        self.calculate_paths(start)

    def calculate_paths(self, start):
        self.dist[start] = 0
        for i in range(self.g.V):
            for j in range(self.g.V):
                for edge in self.g.adj(j):
                    self.relex_edge(edge)

    def relex_edge(self, edge):
        v = edge.either()
        w = edge.other(v)
        if self.dist[w] > self.dist[v] + edge.wt:
            self.dist[w] = self.dist[v] + edge.wt
            self.prev[w] = v

    def get_path(self, w):
        path = []
        i = w
        while i is not None:
            path.append(i)
            i = self.prev[i]
        return list(reversed(path))


class TestBellmanFord(unittest.TestCase):
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
        self.assertListEqual(BellmanFord(g, 0).get_path(3), [0, 2, 3])


if __name__ == '__main__':
    unittest.main()

