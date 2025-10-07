# Импортирует функции из module5.

from module5 import power, square_root, area_of_circle


def volume_of_sphere(radius):
    """Вычисляет объем сферы."""
    return (4 / 3) * 3.1416 * power(radius, 3)


def hypotenuse(a, b):
    """Вычисляет гипотенузу прямоугольного треугольника."""
    return square_root(a ** 2 + b ** 2)


def perimeter_of_rectangle(length, width):
    """Вычисляет периметр прямоугольника."""
    return 2 * (length + width)
