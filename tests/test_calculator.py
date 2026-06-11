from calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(10, 0) is None


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_multiply_float_numbers():
    assert multiply(2.5, 4) == 10.0


def test_subtract_negative_result():
    assert subtract(3, 10) == -7
