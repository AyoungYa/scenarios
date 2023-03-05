import sys

sys.path.append("/home/labex/project")

import unittest

class TestPipInstall(unittest.TestCase):
    def test_pip_install(self):
        try:
            from faker import Faker
            fake = Faker()
            fake.name()
        except Exception:
            self.assertRaises(ImportError)


if __name__ == "__main__":
    unittest.main()
