import pytest

from Kasir import *
from User import *

Kasir1 = Kasir()


def test_1():
    Kasir1 = Kasir()
    assert Kasir1.testTotalIsiKranjang() == float(50000)


def test_2():
    assert Kasir1.testIsiKranjang("susu") == True


def test_3():
    assert Kasir1.testIsiStok("roti") == False

# pytest Test2.py
