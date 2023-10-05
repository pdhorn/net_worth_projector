import unittest
from net_worth_projector.asset import Asset

class TestAsset(unittest.TestCase):
    def setUp(self):
        self.asset = Asset("one", 100, .10, "pre")

    def test_grow(self):
        for _ in range(12):
            self.asset.grow()
        self.assertEqual(self.asset.balance, 110)
    

if __name__ == '__main__':
    unittest.main()
