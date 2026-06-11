VALID_OPERATIONS = ["+", "-", "*", "/"]


def get_number(message):
    try:
        return float(input(message))
    except ValueError:
        print("Нужно ввести число")
        return None


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None

    return a / b


def calculate(a, b, operation):
    if operation == "+":
        return add(a, b)
    elif operation == "-":
        return subtract(a, b)
    elif operation == "*":
        return multiply(a, b)
    elif operation == "/":
        return divide(a, b)

    return None


def main():
    while True:
        operation = input("Операция (+, -, *, /) или q для выхода: ")

        if operation == "q":
            print("Выход")
            break

        if operation not in VALID_OPERATIONS:
            print("Неизвестная операция")
            continue

        a = get_number("Первое число: ")

        if a is None:
            continue

        b = get_number("Второе число: ")

        if b is None:
            continue

        result = calculate(a, b, operation)

        if result is None:
            print("На ноль делить нельзя")
        else:
            print(result)


if __name__ == "__main__":
    main()
