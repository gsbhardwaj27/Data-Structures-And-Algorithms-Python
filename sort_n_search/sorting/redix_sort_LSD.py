# Items to sort has to be of fixed length
# For fixed set of distinct values
# here chars sorting can be done in order of n
# space complexity of n
# stable sort

import unittest
import string
import random


class LSDRedix:
    def __init__(self, items):
        self.aux = [None]*len(items)
        self.a = items
        self.redix_sort()

    def redix_sort(self):
        sz = len(self.a)
        char_set_size = len(string.ascii_lowercase)
        count = [0]*(char_set_size+1)
        for d in range(len(self.a[0])-1, -1, -1):
            count = [0]*(char_set_size+1)
            for i in range(sz):
                count[ ord(self.a[i][d])-97+1 ] += 1
    
            for i in range(char_set_size):
                count[i+1] += count[i]

            for i in range(sz):
                self.aux[count[ord(self.a[i][d])-97]] = self.a[i]
                count[ord(self.a[i][d])-97]+=1

            for i in range(sz):
                self.a[i] = self.aux[i]
    
    def get_sorted_data(self):
        return self.a


class TestLSDRedix(unittest.TestCase):
    def test_name_sorting(self):
        name_length = 5
        names_length = 10
        names = [''.join(random.sample(string.ascii_lowercase, name_length)) for x in range(names_length)]
        self.assertListEqual(sorted(names), LSDRedix(names).get_sorted_data())
    

if __name__ == '__main__':
    unittest.main()
