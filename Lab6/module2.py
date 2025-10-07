# Импортирует функции из module3.

from module3 import area_of_triangle, circumference_of_circle, quadratic_formula


def volume_of_cylinder(radius, height):
    """Вычисляет объем цилиндра."""
    return 3.1416 * radius ** 2 * height


def surface_area_of_cube(side):
    """Вычисляет площадь поверхности куба."""
    return 6 * side ** 2


def mean_of_list(numbers):
    """Вычисляет среднее значение списка."""
    return sum(numbers) / len(numbers)
