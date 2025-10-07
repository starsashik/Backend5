# Содержит функцию для шага 2, демонстрирующую работоспособность импортов.

from module1 import max_in_list, min_in_list, sort_list
from module2 import mean_of_list  # Для демонстрации более глубокого импорта
from module7 import is_prime  # Прямой импорт, но дерево идет через цепочку


def demonstrate_imports():
    """Демонстрирует работоспособность импортов из дерева модулей. (Шаг 2)"""
    numbers = [5, 3, 8, 1, 9]
    print(f"Максимум: {max_in_list(numbers)}")
    print(f"Минимум: {min_in_list(numbers)}")
    print(f"Отсортированный список: {sort_list(numbers)}")
    print(f"Среднее: {mean_of_list(numbers)}")
    print(f"Является ли 7 простым? {is_prime(7)}")  # Из самого глубокого модуля
