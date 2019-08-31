import unittest
import random
from timeit import default_timer as timer
from sorting import (selection_sort,
                     insertion_sort,
                     shell_sort,
                     merge_sort,
                     merge_sort_optimizations,
                     merge_sort_bottom_up)

ALGOS = [selection_sort,
         insertion_sort,
         shell_sort,
         merge_sort,
         merge_sort_optimizations,
         merge_sort_bottom_up]


class testSorting(unittest.TestCase):

    def setUp(self):
        self.none = None
        self.empty = []
        self.items_one = [random.randint(1, 1000)]
        self.items_two = [random.randint(1, 1000), random.randint(1, 1000)]
        self.items_small = [random.randint(1, 100) for x in range(20)]
        self.items_large = [random.randint(1, 200000) for x in range(10000)]

    def test_is_sorted(self):
        for algo in ALGOS:
            print(algo)
            self.assertIsNone(algo.sort(self.none))
            self.assertEqual(algo.sort(self.empty), self.empty)
            self.assertEqual(algo.sort(self.items_one),
                             self.items_one)
            self.assertEqual(algo.sort(self.items_two),
                             sorted(self.items_two))
            self.assertEqual(algo.sort(self.items_small),
                             sorted(self.items_small))
            self.items_large = [random.randint(1, 200000) for x in range(1000)]
            start = timer()
            sorted_data = algo.sort(self.items_large)
            print("Time taken  = ", timer()-start)
            self.assertEqual(sorted_data,
                             sorted(self.items_large))

    def test_large_numbers(self):
        print("--------Large Numbers---------")
        for algo in ALGOS:
            print(algo)
            self.items_large = [random.randint(1, 200000) for x in range(1000)]
            start = timer()
            sorted_data = algo.sort(self.items_large)
            print("Time taken  = ", timer()-start)
            self.assertEqual(sorted_data,
                             sorted(self.items_large))

    def test_nearly_sorted_numbers(self):
        print("--------Large almost sorted Numbers---------")
        for algo in ALGOS:
            print(algo)
            almost_sorted = self.nearly_sorted_numbers(2000)
            start = timer()
            sorted_data = algo.sort(almost_sorted)
            print("Time taken  = ", timer()-start)
            self.assertEqual(sorted_data,
                             sorted(almost_sorted))

    def nearly_sorted_numbers(self, n):
        if n >= 100:
            x = n//10
        elif n >= 10:
            x = 9
        else:
            x = 4
        numbers = []
        for i in range(1, n):
            numbers.append(random.randint(i+n//20, i+n//10))
        return numbers


if __name__ == '__main__':
    unittest.main()
