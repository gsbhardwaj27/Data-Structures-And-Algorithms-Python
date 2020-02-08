# Breath First Traversal of Graph
# Limited by memory available
# complexity

import unittest
from graph import Graph
from collections import deque

class BFS:
    def __init__(self, g):
        self.g = g
        
    def bfs(self, v):
        data = []
        q = deque()
        q.append(v)
        done = [False for i in range(self.g.V)]
        while q:
            node = q.popleft()
            data.append(node)
            done[node] = True
            for each in self.g.adj(node):
                if not done[each]:
                    q.append(each)
        return data


class TestBFS(unittest.TestCase):
    def test_bfs(self):
        g = Graph(10)
        g.add_edge(1, 2)
        g.add_edge(2, 4)
        g.add_edge(2, 6)
        g.add_edge(7, 8)
        g.add_edge(1, 8)
        self.assertListEqual(BFS(g).bfs(1), [1, 2, 8, 4, 6, 7])
    

if __name__ == '__main__':
    unittest.main()
