import unittest
from net_worth_projector.month import Month

class TestMonth(unittest.TestCase):
    def setUp(self):
        self.december = Month(2020, 12)
        self.january = Month(2021, 1)

    def test_repr(self):
        self.assertEqual(self.january.__repr__(), '2021-01')
    
    def test_next(self):
        self.assertEqual(self.december.next(), self.january)
    
    def test_gt(self):
        self.assertTrue(self.january > self.december)
        self.assertFalse(self.december > self.january)
        self.assertTrue(self.january >= self.january)
        self.assertFalse(self.december > self.december)

if __name__ == '__main__':
    unittest.main()
