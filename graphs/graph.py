import unittest


class Graph:
    def __init__(self, v):
        self.V = v
        self.E = [[] for x in range(v+1)]

    def add_edge(self, v, w):
        self.E[v].append(w)
        self.E[w].append(v)

    def adj(self, v):
        return self.E[v]

    def degree(self, v):
        return len(self.E[v])

    def are_adj(self, v, w):
        for each in self.adj(v):
            if each==w:
                return True
        return False

    def populate_graph(self):
        edge_count = int(input())
        for i in range(edge_count()):
            v, w = map(int, (input().strip().split(' ')))
            self.add_edge(v, w)
    

class TestGraph(unittest.TestCase):
    def test_adj(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)

        self.assertTrue(g.are_adj(1, 8))
        self.assertFalse(g.are_adj(1, 10))

    def test_degree(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)

        self.assertTrue(g.degree(1)==2)
        self.assertTrue(g.degree(10)==0)
        self.assertTrue(g.degree(7)==1)


if __name__ == '__main__':
    unittest.main()    
