# Импортирует функции из module2, начало дерева.

from module2 import volume_of_cylinder, surface_area_of_cube, mean_of_list


def max_in_list(numbers):
    """Находит максимум в списке."""
    return max(numbers)


def min_in_list(numbers):
    """Находит минимум в списке."""
    return min(numbers)


def sort_list(numbers):
    """Сортирует список."""
    return sorted(numbers)
