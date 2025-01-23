import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from src.calculator import *
def test_smoke_add():
    # Smoke test for add function
    result = add(1, 1)
    assert result == 2

def test_smoke_subtract():
    # Smoke test for subtract function
    result = subtract(2, 1)
    assert result == 1

def test_smoke_multiply():
    # Smoke test for multiply function
    result = multiply(2, 2)
    assert result == 4

def test_smoke_divide():
    # Smoke test for divide function
    result = divide(4, 2)
    assert result == 2
