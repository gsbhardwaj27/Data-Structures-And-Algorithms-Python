import unittest
import random


class MinIndexedHeap:
    def __init__(self, items):
        self.keys = [item for item in items]
        self.pq = [None]*len(self.keys)
        self.qp = [None]*len(self.keys)
        self.size = 0
        for ki, key in enumerate(self.keys):
            self.add_item(ki, key)

    def add_item(self, ki, value):
        self.pq[ki] = self.size
        self.qp[self.size] = ki
        self.size += 1
        self.swim(self.size-1)

    def swim(self, idx):
        while idx > 0  and self.less(idx, (idx-1)//2):
            self.swap(idx, (idx-1)//2)
            idx = (idx-1)//2

    def sink(self, idx):
        while idx*2+1 < self.size:
            mn_idx = 2*idx+1
            if idx*2+2 < self.size and self.less(idx*2+2, mn_idx):
                mn_idx = idx*2+2
            if self.less(mn_idx, idx):
                self.swap(mn_idx, idx)
            else:
                break

    def less(self, i, j):
        if self.keys[self.qp[i]] < self.keys[self.qp[j]]:
            return True
        else:
            return False

    def swap(self, i, j):
        self.pq[self.qp[i]], self.pq[self.qp[j]] = self.pq[self.qp[j]], self.pq[self.qp[i]]
        self.qp[i], self.qp[j] = self.qp[j], self.qp[i]

    def del_min(self):
        data = None
        if not self.empty():
            data = self.keys[self.qp[0]]
            self.swap(0, self.size-1)
            self.pq[self.qp[self.size-1]] = None
            self.qp[self.size-1] = None
            self.size -= 1
            self.sink(0)
        return data

    def empty(self):
        return self.size==0

    def decrease_key(self, ki, key):
        self.keys[ki] = key
        self.swim(self.pq[ki])


class TestMinIndexedHeap(unittest.TestCase):
    def setUp(self):
        size = 5
        self.arr = [random.randint(0, size*size) for x in range(size)]

    def test_min_heap(self):
        min_heap = MinIndexedHeap(self.arr)
        self.assertEqual(min_heap.empty(), False)

        test = []
        while not min_heap.empty():
            test.append(min_heap.del_min())
        self.assertListEqual(sorted(self.arr), test)

    def test_min_heap_decrease_key(self):
        min_heap = MinIndexedHeap(self.arr)
        self.assertEqual(min_heap.empty(), False)

        idx = random.randint(0, len(self.arr)-1)
        tmp_key = self.arr[idx] = self.arr[idx]//2
        min_heap.decrease_key(idx, tmp_key)

        test = []
        while not min_heap.empty():
            test.append(min_heap.del_min())
        self.assertListEqual(sorted(self.arr), test)

if __name__ == '__main__':
    unittest.main()
