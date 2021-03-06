import unittest
from more_functions import validate_input_in_fucntions as topic4


class MyTestClass(unittest.TestCase):
    def test_score_input_test_score_valid(self):
        self.assertEqual(topic4.score_input('vickilee', ), 'vickilee : 0')

    def test_score_input_test_score_below_range(self):
        self.assertEqual(topic4.score_input('vickilee',110),'Invalid test score, try again')

    def test_score_input_test_score_above_range(self):
        self.assertEqual(topic4.score_input('vickilee', 110), 'Invalid test score, try again')

    def test_test_score_non_numeric(self):
        self.assertEqual(topic4.score_input('vickilee','hello'), 'Invalid test score, try again')


if __name__ == '__main__':
    unittest.main()
