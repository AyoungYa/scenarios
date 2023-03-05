import sys

from shape import Shape

sys.path.append("/home/labex/project")

import unittest


class Testshape(unittest.TestCase):
    def test_init_method(self):
        length = 3
        shape = Shape(length)
        self.assertEqual(shape.length, length)
        length = 5
        shape = Shape(length)
        self.assertEqual(shape.length, length)

    def test_area_method(self):
        length = 3
        shape = Shape(length)
        with self.assertRaises(NotImplementedError):
            shape.area()


if __name__ == "__main__":
    unittest.main()
