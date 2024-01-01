import unittest
from age_difference import age_difference

class TestAgeDifference(unittest.TestCase):

    def test_age_difference(self):
        # self.assertEqual(age_difference([18, 25, 50, 35, 40]), (18, 50))
        # self.assertEqual(age_difference([30, 20, 25, 40, 45, 50]), (20, 50))
        # self.assertEqual(age_difference([10, 5, 8, 20, 15, 25]), (5, 25))

        ''''''
        '''計算並返回最年長成員和最年輕成員的年齡差'''
        self.assertEqual(age_difference([18, 25, 50, 35, 40]), (32))
        self.assertEqual(age_difference([30, 20, 25, 40, 45, 50]), (30))
        self.assertEqual(age_difference([10, 5, 8, 20, 15, 25]), (20))

if __name__ == '__main__':
    unittest.main()
