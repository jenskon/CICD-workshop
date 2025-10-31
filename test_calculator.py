import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_summation(calculator):
    assert 10 == calculator.summation(5, 5)

def test_summation_0(calculator):
    assert 0 == calculator.summation(5, -5)

def test_difference(calculator):
    assert 4 == calculator.difference(8, 4)

def test_difference_0(calculator):
    assert 0 == calculator.difference(4, 4)

def test_product(calculator):
    assert 20 == calculator.product(4, 5)

def test_product_zero(calculator):
    assert 0 == calculator.product(0, 5)

def test_quotient(calculator):
    assert 2 == calculator.quotient(10, 5)

def test_quotient_float(calculator):
    assert 2.5 == calculator.quotient(5, 2)
