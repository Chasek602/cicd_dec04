import sys
from pathlib import Path
import pytest

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))


from app import add, sub, mul, div, log, square, sin, cos, sqrt, percentage

def test_add():
    assert add(5, 6) == 11

def test_add2():
    assert add(5, 6) != 10


# basic ops

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(3, 4) == 12

def test_div():
    assert div(12, 3) == 4

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(5, 0)


# advanced ops

def test_square():
    assert square(5) == 25

def test_sqrt():
    assert sqrt(9) == 3

def test_sqrt_negative():
    with pytest.raises(ValueError):
        sqrt(-1)

def test_log():
    import math
    assert math.isclose(log(10), math.log(10))

def test_log_zero():
    with pytest.raises(ValueError):
        log(0)

def test_log_negative():
    with pytest.raises(ValueError):
        log(-5)

def test_sin():
    assert sin(0) == 0

def test_cos():
    assert cos(0) == 1

def test_percentage():
    assert percentage(10, 200) == 20
