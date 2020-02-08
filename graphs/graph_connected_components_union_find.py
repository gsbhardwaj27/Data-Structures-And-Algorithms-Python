# Connected components using grapth traversal
# Here i am using depth first graph traversal

import unittest

from graph import Graph

class UnionFind:
    def __init__(self, v): 
        self.wts = [1 for x in range(v)]
        self.roots = [x for x in range(v)]

    def root(self, node):
        p = node
        while p != self.roots[p]:
            self.roots[p] = self.roots[self.roots[p]]
            p = self.roots[p]
        return p

    def union(self, v, w):
        rv = self.root(v)
        rw = self.root(w)
        if self.wts[rv] >= self.wts[rw]:
            self.roots[rw] = self.roots[rv]
            self.wts[rv] += self.wts[rw]
        else:
            self.roots[rv] = self.roots[rw]
            self.wts[rw] += self.wts[rv]

    def are_connected(self, v, w):
        return self.roots[v] == self.roots[w]
             

class TestContCompUnionFind(unittest.TestCase):
    def test_cc(self):
        uf = UnionFind(8)
        uf.union(0, 1)
        uf.union(0, 5)
        uf.union(0, 2)
        uf.union(2, 3)
        uf.union(6, 7)
       
        self.assertFalse(uf.are_connected(0, 4)) 
        self.assertTrue(uf.are_connected(0, 3)) 
        self.assertFalse(uf.are_connected(2, 7)) 
        self.assertFalse(uf.are_connected(4, 7)) 
        self.assertTrue(uf.are_connected(6, 7)) 


if __name__ == '__main__':
    unittest.main()
