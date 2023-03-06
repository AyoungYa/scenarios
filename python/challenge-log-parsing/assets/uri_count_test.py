import sys

sys.path.append("/home/labex/project")

import unittest
from uri_count import uri_count


class TestReadLog(unittest.TestCase):
    def test_uri_count(self):
        file_name = 'x.log'
        self.assertRaises(uri_count(file_name), FileNotFoundError)

        file_name = 'access.log'
        result = uri_count(file_name)
        self.assertTrue(isinstance(result, dict))
        self.assertEqual(len(result.keys()), 5)

        result = {
            "/create/order":  199,
            "/query/order/info":  192,
            "/service/pricing":  183,
            "/hello/user":  239,
            "/user/info":  186
        }

        for k, v in result.items():
            self.assertTrue(k in result.keys)
            self.assertEqual(v, result.get(k))

if __name__ == "__main__":
    unittest.main()
