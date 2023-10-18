import unittest
from ordered_list import *


class TestLab4(unittest.TestCase):

    def test_simple(self):
        t_list = DoublyOrderedList()
        t_list.add(10)
        t_list.add(15)
        t_list.add(13)
        self.assertEqual(t_list.python_list(), [10, 13, 15])
        # self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.index(10), 0)
        self.assertTrue(t_list.search(10))
        self.assertFalse(t_list.is_empty())
        # self.assertEqual(t_list.python_list_reversed(), [10])
        self.assertTrue(t_list.remove(10))
        t_list.add(10)

        print(t_list)
        self.assertEqual(t_list.pop(0), 10)
        print(t_list)


if __name__ == '__main__':
    unittest.main()