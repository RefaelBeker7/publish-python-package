from py_package import *

def test_f2c():
    assert f2c(32) == 0.0

def test_c2f():
    assert c2f(0) == 32.0