import unittest
import random


class MinHeap:
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def swim(self, idx):
        while idx != 1 and self.arr[idx//2] > self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx//2

    def sink(self, idx):
        while idx*2 <= self.size:
            mn_idx = idx*2
            if idx*2+1 <= self.size and self.arr[idx*2+1] < self.arr[idx*2]:
                mn_idx = idx*2+1
            if self.arr[mn_idx] < self.arr[idx]:
                self.arr[mn_idx], self.arr[idx] = self.arr[idx], self.arr[mn_idx]
                idx = mn_idx
            else:
                break

    def get_min(self):
        if self.size > 0:
            return self.arr[1]
        else:
            return None

    def del_min(self):
        if self.size > 0:
            mn = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            self.sink(1)
            return mn

    def insert(self, val):
        if len(self.arr)-1 <= self.size:
            self.arr.append(val)
        else:
            self.arr[self.size+1] = val
        self.size += 1
        self.swim(self.size)

    def empty(self):
        return self.size == 0


class TestMinHeap(unittest.TestCase):
    def setUp(self):
        size = 100
        self.arr = [random.randint(0, size*size) for x in range(size)]

    def test_min_heap(self):
        min_heap = MinHeap()
        self.assertEqual(min_heap.empty(), True)

        for each in self.arr:
            min_heap.insert(each)

        test = []
        while not min_heap.empty():
            test.append(min_heap.del_min())
        self.assertListEqual(sorted(self.arr), test)


if __name__ == '__main__':
    unittest.main()
