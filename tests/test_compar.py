import pytest
from comparisons import sort_by_year, sort_by_title

import unittest

def compare_numbers(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

def compare_strings(a, b):
    return (a.lower() > b.lower()) - (a.lower() < b.lower())


class ComparatorTests(unittest.TestCase):
    def test_compare_numbers(self):
        self.assertEqual(compare_numbers(10, 5), 1)
        self.assertEqual(compare_numbers(5, 10), -1)
        self.assertEqual(compare_numbers(5, 5), 0)

    def test_compare_strings(self):
        self.assertEqual(compare_strings("apple", "banana"), -1)
        self.assertEqual(compare_strings("banana", "apple"), 1)
        self.assertEqual(compare_strings("apple", "apple"), 0)
        self.assertEqual(compare_strings("Apple", "apple"), 0)
        self.assertEqual(compare_strings("apple", "Apple"), 0)

if __name__ == '__main__':
    unittest.main()
