import sys
from unittest.mock import patch

from area import cal_area
sys.path.append("/home/labex/project")

import unittest


def get_input(text):
    return input(text)

class TestSubclass(unittest.TestCase):
    @patch("get_input", return_value="1 10")
    def test_circle(self, input_str):
        shape, area = cal_area(input_str)
        self.assertEqual("circle", shape)
        self.assertTrue(abs(area - 3.14 * 10 * 10) < 0.1)

    @patch("get_input", return_value="2 10")
    def test_sqaure(self, input_str):
        shape, area = cal_area(input_str)
        self.assertEqual("square", shape)
        self.assertEqual(100, area)


if __name__ == "__main__":
    unittest.main()
