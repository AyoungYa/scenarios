import sys

sys.path.append("/home/labex/project")

import unittest
from read_log import read_log


class TestReadLog(unittest.TestCase):
    def test_read_log(self):
        file_name = 'x.log'
        self.assertRaises(read_log(file_name), FileNotFoundError)

        file_name = 'access.log'
        self.assertEqual(read_log(file_name), 1997)


if __name__ == "__main__":
    unittest.main()
