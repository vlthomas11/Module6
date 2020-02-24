import unittest
from more_functions import more_functions as topic3


class MyTestClass(unittest.TestCase):
    def test_multiple_string(self):
        self.assertEqual(topic3.multiply_string('vickilee', 3), 'vickileevickileevickilee')
    def test_multiply_string_fail(self):
        self.assertIsNot(topic3.multiply_string('vickilee',5),'vickileevickilee')
    def test_multiply_string2(self):
        self.assertEqual(topic3.multiply_string('vickilee',4),'vickilee'*4)
