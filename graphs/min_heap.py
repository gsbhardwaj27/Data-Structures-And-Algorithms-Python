import unittest
import random

class MinHeap:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        pos = len(self.items)-1 
        self.swim(pos)

    def del_min(self):
        val = None
        if self.items:
            val = self.items[0]
            if len(self.items) > 1:
                self.items[0] = self.items.pop()
                self.sink(0)
            else:
                self.items.pop()
        return val
    
    def swim(self, pos):
        par = (pos-1)//2
        while pos > 0 and self.items[pos] < self.items[(pos-1)//2]:
            self.items[(pos-1)//2], self.items[pos] = self.items[pos], self.items[(pos-1)//2]
            pos = (pos-1)//2

    def sink(self, pos):
        while pos*2+1 < len(self.items):
            next = pos
            if pos*2+1 < len(self.items) and self.items[pos*2+1] < self.items[next]:
                next = pos*2+1
            if pos*2+2 < len(self.items) and self.items[pos*2+2] < self.items[next]:
                next = pos*2+2
            
            self.items[pos], self.items[next] = self.items[next], self.items[pos]
            if next == pos:
                break
            pos = next            

    def is_empty(self):
        return not self.items

    
class TestHeap(unittest.TestCase):
    def test_sorting(self):
        size = 300
        items = [random.randint(1, size*size) for i in range(size)] 
        sorted_items = []
        heap = MinHeap()
        for each in items:
            heap.add_item(each)
        while not heap.is_empty():
            sorted_items.append(heap.del_min())
        self.assertListEqual(sorted_items, sorted(items))

if __name__ == '__main__':
    unittest.main()
