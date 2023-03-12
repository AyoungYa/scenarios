import sys

sys.path.append("/home/labex/project")

import unittest
from basket_weight import basket_weight


class TestBasketWeight(unittest.TestCase):
    def test_basket_weight(self):
        baskets = {}
        result = basket_weight(baskets)
        self.assertTrue(not result)
        self.assertEqual({}, result)
        self.assertEqual(0, len(result.key()))

        baskets = {
            "apple": [1, 2.3, 4, 5],
            "orange": [3],
            "banana": [4, 5, 6]
        }
        result = basket_weight(baskets)
        self.assertEqual(3, result.keys())
        self.assertEqual(15, result[0]['weight'])
        self.assertEqual(3, result[2]["orange"])

if __name__ == "__main__":
    unittest.main()
