import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.calculator import *
def test_smoke_add():
    result = add(1, 1)
    assert result == 2

def test_smoke_subtract():
    result = subtract(2, 1)
    assert result == 1

def test_smoke_multiply():
    result = multiply(2, 2)
    assert result == 4

def test_smoke_divide():

    result = divide(4, 2)
    assert result == 2
