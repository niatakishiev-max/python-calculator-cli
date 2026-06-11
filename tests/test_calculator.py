import pytest

from calculator import add, subtract, multiply, divide, get_number


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-2, -3, -5),
    (2.5, 4, 6.5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 4, 6),
    (3, 10, -7),
    (-5, -2, -3),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (3, 4, 12),
    (2.5, 4, 10.0),
    (-2, 5, -10),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (9, 3, 3),
    (7.5, 2.5, 3),
    (-10, 2, -5),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero():
    assert divide(10, 0) is None


def test_get_number_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda message: "10")

    assert get_number("Введите число: ") == 10.0


def test_get_number_invalid(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda message: "abc")

    assert get_number("Введите число: ") is None

    captured = capsys.readouterr()
    assert "Нужно ввести число" in captured.out
