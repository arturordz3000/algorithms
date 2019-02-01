import unittest
from merge_sort import *

class MergeSort(unittest.TestCase):
    def test_merge_sort_with_elements(self):
        self.assertEqual(merge_sort([1,5,8,3,5,9]), [1,3,5,5,8,9])
        self.assertEqual(merge_sort([9,15,1,85,74,789,1111,3,365]), [1,3,9,15,74,85,365,789,1111])
    
    def test_merge_sort_empty_array(self):
        self.assertEqual(merge_sort([]), [])

    def test_merge_sort_single_element(self):
        self.assertEqual(merge_sort([1]), [1])

    def test_merge_sort_decreasing_with_elements(self):
        self.assertEqual(merge_sort_decreasing([1,5,8,3,5,9]), [9,8,5,5,3,1])
        self.assertEqual(merge_sort_decreasing([9,15,1,85,74,789,1111,3,365]), [1111,789,365,85,74,15,9,3,1])
