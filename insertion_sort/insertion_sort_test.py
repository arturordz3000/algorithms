import unittest
from insertion_sort import *

class InsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort([1,5,8,3,5,9]), [1,3,5,5,8,9])
        self.assertEqual(insertion_sort([9,15,1,85,74,789,1111,3,365]), [1,3,9,15,74,85,365,789,1111])
