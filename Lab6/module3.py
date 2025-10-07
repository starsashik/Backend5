# Импортирует функции из module4.

from module4 import volume_of_sphere, hypotenuse, perimeter_of_rectangle


def area_of_triangle(base, height):
    """Вычисляет площадь треугольника."""
    return 0.5 * base * height


def circumference_of_circle(radius):
    """Вычисляет длину окружности."""
    return 2 * 3.1416 * radius


def quadratic_formula(a, b, c):
    """Решает квадратное уравнение, возвращает корни."""
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    root1 = (-b + discriminant ** 0.5) / (2 * a)
    root2 = (-b - discriminant ** 0.5) / (2 * a)
    return root1, root2
