# Items to sort has to be of fixed length
# For fixed set of distinct values
# here chars sorting can be done in order of n
# space complexity of n
# stable sort

import unittest
import string
import random


class MSDRedix:
    def __init__(self, items):
        self.aux = [None]*len(items)
        self.a = items
        self.redix_sort_msd(0, len(items)-1, 0)

    def redix_sort_msd(self, lo, hi, d):
        if hi > lo:
            char_set_size = len(string.ascii_lowercase)
            count = [0]*(char_set_size+2)

            for i in range(lo, hi+1):
                count[self.get_val(self.a[i], d)+2] += 1
    
            for i in range(len(count)-1):
                count[i+1] += count[i]

            for i in range(lo, hi+1):
                val = self.get_val(self.a[i], d)
                self.aux[lo+count[val+1]] = self.a[i]
                count[val+1]+=1

            for i in range(lo, hi+1):
                self.a[i] = self.aux[i]
            
            for i in range(char_set_size):
                self.redix_sort_msd(lo+count[i], lo+count[i+1]-1, d+1)
    
    def get_val(self, l, i):
        if i < len(l):
            return ord(l[i])-97
        else:
            return -1

    def get_sorted_data(self):
        return self.a


class TestMSDRedix(unittest.TestCase):
    def test_name_sorting(self):
        name_length = 10
        names_length = 50
        names = [''.join(random.sample(string.ascii_lowercase, random.randint(1, 10))) for x in range(names_length)]
        self.assertListEqual(sorted(names), MSDRedix(names).get_sorted_data())
    

if __name__ == '__main__':
    unittest.main()
