import unittest

from source_file.inner_functions_assignment import measurements


class MyTestCse(unittest.TestCase):
    def test_measurements_rectangle(self):
        self.assertEqual(measurements([2.1, 3.4]), "Perimeter = 11.0 Area = 7.14")

    def test_measurements_square(self):
        self.assertEqual(measurements([3.5]), "Perimeter = 14.0 Area = 12.25")
