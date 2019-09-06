import unittest
import random


class MaxHeap:
    def __init__(self):
        self.arr = [0]
        self.size = 0

    def swim(self, idx):
        while idx != 1 and self.arr[idx//2] < self.arr[idx]:
            self.arr[idx], self.arr[idx//2] = self.arr[idx//2], self.arr[idx]
            idx = idx//2

    def sink(self, idx):
        while idx*2 <= self.size:
            mx_idx = idx*2
            if idx*2+1 <= self.size and self.arr[idx*2+1] > self.arr[idx*2]:
                mx_idx = idx*2+1
            if self.arr[mx_idx] > self.arr[idx]:
                self.arr[mx_idx], self.arr[idx] = self.arr[idx], self.arr[mx_idx]
                idx = mx_idx
            else:
                break

    def get_max(self):
        if self.size > 0:
            return self.arr[1]
        else:
            return None

    def del_max(self):
        if self.size > 0:
            mx = self.arr[1]
            self.arr[1] = self.arr[self.size]
            self.arr[self.size] = None
            self.size -= 1
            self.sink(1)
            return mx

    def insert(self, val):
        if len(self.arr)-1 <= self.size:
            self.arr.append(val)
        else:
            self.arr[self.size+1] = val
        self.size += 1
        self.swim(self.size)

    def empty(self):
        return self.size == 0


class TestMaxHeap(unittest.TestCase):
    def setUp(self):
        size = 100
        self.arr = [random.randint(0, size*size) for x in range(size)]

    def test_max_heap(self):
        max_heap = MaxHeap()
        self.assertEqual(max_heap.empty(), True)

        for each in self.arr:
            max_heap.insert(each)

        test = []
        while not max_heap.empty():
            test.append(max_heap.del_max())
        self.assertListEqual(sorted(self.arr, reverse=True), test)


if __name__ == '__main__':
    unittest.main()
