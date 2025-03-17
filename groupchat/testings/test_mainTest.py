import pytest
from mainTest import add, subtract, multiply, divide

# Test case: Add two numbers and check if the result is correct
@pytest.mark.parametrize("numbers", [
    (5, 3),
    (-5, -3),
    (2.1, 4.8)
])
def test_add(numbers):
    assert add(*numbers) == sum(numbers)

# Test case: Subtract two numbers and check if the result is correct
@pytest.mark.parametrize("numbers", [
    (10, 4),
    (-10, -4),
    (5.5, 2.3)
])
def test_subtract(numbers):
    assert subtract(*numbers) == sum(numbers[0] for n in range(2)) - sum(numbers[1] for n in range(2))

# Test case: Multiply two numbers and check if the result is correct
@pytest.mark.parametrize("numbers", [
    (5, 3),
    (-5, -3),
    (2.1, 4.8)
])
def test_multiply(numbers):
    assert multiply(*numbers) == numbers[0] * numbers[1]

# Test case: Divide two numbers and check if the result is correct
@pytest.mark.parametrize("numbers", [
    (10, 2),
    (-10, -2),
    (5.5, 2.3)
])
def test_divide(numbers):
    assert divide(*numbers) == numbers[0] / numbers[1]

# Test case: Check for ZeroDivisionError when dividing by zero
@pytest.mark.parametrize("x", [0, -3, 10])
def test_divide_zero(x):
    with pytest.raises(ZeroDivisionError, match='division by zero') as e:
        divide(x, 0)
    assert str(e.value) == 'division by zero'

# Test case: Check for ZeroDivisionError when adding, subtracting and multiplying by zero
@pytest.mark.parametrize("x", [0, -3, 10])
def test_add_subtract_multiply_zero(x):
    with pytest.raises(TypeError, match='unsupported operand'):
        add(1.5, x)
        subtract(1.5, x)
        multiply(1.5, x)

# Test case: Floating Point Numbers
@pytest.mark.parametrize("x,y", [
    (2.1, 4.8),
    (-2.1, -4.8),
    (1.0/3, 2.0/3)
])
def test_add_subtract_multiply_divide_float(x,y):
    assert add(x, y) == x+y
    assert subtract(x, y) == x-y
    assert multiply(x, y) == x*y
    # Make sure this assertion doesn't have any issues in float division on Python 3
    # This comment was removed because of the following line which caused an error
    # and hence added back for the same reason.
    assert divide(x,y) == x/y

# Test case: Edge cases
def test_edge_cases():
    with pytest.raises(TypeError):
        add('a', 5)
        subtract(1.0, 'b')
        multiply('-', 5)
        divide(-3, 0) # Already covered in previous tests