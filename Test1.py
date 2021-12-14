import unittest

from Kasir import *
from User import *


class Test(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Kasir.testTotalIsiKranjang(self), float(50000))

    def test_2(self):
        self.assertEqual(Kasir.testIsiKranjang(self, "susu"), True)

    def test_3(self):
        self.assertEqual(Kasir.testIsiStok(self, "susu"), True)


if __name__ == "__main__":
    unittest.main()

# python -m unittest Test1
