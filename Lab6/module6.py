# Импортирует функции из module7 для продолжения дерева.

from module7 import calculate_factorial, is_prime, sum_of_digits


def fibonacci_sequence(n):
    """Генерирует последовательность Фибоначчи до n элементов."""
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


def greatest_common_divisor(a, b):
    """Находит НОД двух чисел."""
    while b:
        a, b = b, a % b
    return a


def least_common_multiple(a, b):
    """Находит НОК с использованием НОД."""
    return abs(a * b) // greatest_common_divisor(a, b)
