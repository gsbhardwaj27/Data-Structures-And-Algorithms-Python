import unittest


class UnionFind:
    def __init__(self, n):
        self.arr = [x for x in range(n+1)]
        self.size = [1 for x in range(n+1)]

    def union(self, x, y):
        rx = self.root(x)
        ry = self.root(y)
        if self.size[rx] > self.size[ry]:
            rx, ry = ry, rx
        self.arr[rx] = self.arr[ry]
        self.size[ry] += self.size[rx]

    def root(self, x):
        i = x
        while i != self.arr[i]:
            self.arr[i] = self.arr[self.arr[i]]
            i = self.arr[i]
        return i

    def find(self, x, y):
        return self.root(x) == self.root(y)


class testUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(7)

    def test_uf(self):
        self.uf.union(1, 2)
        self.uf.union(1, 3)
        self.uf.union(1, 4)
        self.uf.union(5, 6)
        self.uf.union(6, 7)
        self.assertEqual(self.uf.find(1, 2), True)
        self.assertEqual(self.uf.find(1, 6), False)
        self.assertEqual(self.uf.find(1, 4), True)
        print(self.uf.size)


if __name__ == '__main__':
    unittest.main()
