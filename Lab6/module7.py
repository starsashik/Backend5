# Самый глубокий модуль в дереве импортов.

def calculate_factorial(n):
    """Вычисляет факториал числа."""
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)


def is_prime(number):
    """Проверяет, является ли число простым."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def sum_of_digits(num):
    """Суммирует цифры числа."""
    return sum(int(digit) for digit in str(num))
