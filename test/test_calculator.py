# COMMAND ----------
with open("/dbfs/FileStore/pythoncalculator/src/calculator.py") as f:
    print(f.read())

# COMMAND ----------
import pytest
import sys

sys.path.append('/FileStore/pythoncalculator/src')

# Import dynamically
calculator = __import__('calculator')

def test_add():
    assert calculator.add(3, 5) == 8
    assert calculator.add(-1, 1) == 0

def test_subtract():
    assert calculator.subtract(10, 5) == 5
    assert calculator.subtract(0, 5) == -5

def test_multiply():
    assert calculator.multiply(4, 3) == 12
    assert calculator.multiply(-2, 3) == -6

def test_divide():
    assert calculator.divide(10, 2) == 5
    with pytest.raises(ValueError):
        calculator.divide(10, 0)


# COMMAND ----------

!pytest /dbfs/FileStore/pythoncalculator/test_calculator.py