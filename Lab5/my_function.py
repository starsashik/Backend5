"""
Задания 1-19: Работа со списками, кортежами и словарями
"""
from typing import List, Tuple, Dict, Any, Callable, Optional
import random


# ---------- СПИСКИ ----------

# Шаг 1
def reverse_list(lst: List[Any]) -> List[Any]:
    """[Шаг 1] Переворачивает список"""
    return lst[::-1]


# Шаг 2
def modify_list(lst: List[Any], indices: Optional[List[int]] = None,
                new_value: Any = None) -> List[Any]:
    """[Шаг 2] Изменяет элементы списка"""
    if indices is None:
        indices = [0]
    for i in indices:
        if 0 <= i < len(lst):
            lst[i] = new_value
    return lst


# Шаг 3
def compare_lists(*lists: List[Any]) -> bool:
    """[Шаг 3] Сравнивает списки"""
    if not lists:
        return True
    first = lists[0]
    return all(lst == first for lst in lists)


# Шаг 4
def slice_list(lst: List[Any], start: int = 0,
               end: Optional[int] = None, step: int = 1) -> List[Any]:
    """[Шаг 4] Возвращает диапазон элементов с обработкой краёв"""
    length_lst = len(lst)
    if end is None:
        end = length_lst
    # корректируем отрицательные и большие значения
    if start < 0:
        start = max(0, length_lst + start)
    if end < 0:
        end = max(0, length_lst + end)
    start = min(max(start, 0), length_lst)
    end = min(max(end, 0), length_lst)
    if step == 0:
        raise ValueError("step не может быть 0")
    return lst[start:end:step]


# Шаг 5
def create_list_from_params(*args: Any) -> List[Any]:
    """[Шаг 5] Создаёт список из переданных параметров"""
    return list(args)


# Шаг 6
def insert_element(lst: List[Any],
                   element: Any, position: int = 0) -> List[Any]:
    """[Шаг 6] Вставляет элемент в заданную позицию"""
    if position < 0:
        position = max(0, len(lst) + position)
    lst.insert(position, element)
    return lst


# Шаг 7
def merge_and_sort_lists(*lists: List[Any], reverse: bool = False,
                         key: Optional[Callable[[Any], Any]] = None) -> List[Any]:
    """[Шаг 7] Объединяет и сортирует списки; можно передать key"""
    merged: List[Any] = []
    for element in lists:
        merged.extend(element)
    return sorted(merged, key=key, reverse=reverse)


# Шаг 8
def random_list_process() -> Tuple[List[int], int, int]:
    """[Шаг 8] Создаёт случайный список. Если длина нечётная —
    возвращает (список, центральный элемент, количество равных центральному)."""
    while True:
        length = random.randint(2, 10)
        lst: List[int] = [random.randint(0, 9) for _ in range(length)]
        if len(lst) % 2 == 1:
            mid_index = len(lst) // 2
            middle = lst[mid_index]
            count = lst.count(middle)
            return lst, middle, count
        # else:
        #     print("Создан список четной длины")
        # делает вывод не красивым


# Шаг 9
def append_and_trim(main_list: List[Any], *lists: List[Any],
                    threshold: int = 10) -> List[Any]:
    """[Шаг 9] Прибавляет другие списки к первому; если
    длина > threshold — обрезает до threshold"""
    for element in lists:
        main_list.extend(element)
    if len(main_list) > threshold:
        del main_list[threshold:]
    return main_list


# ---------- ШАГ 10: сортировки (минимум 6, минимум 3 используют map()) ----------

def sort_by_length(lst: List[str]) -> List[str]:
    """[Шаг 10] Сортировка по длине строк"""
    return sorted(lst, key=len)


def sort_by_last_char(lst: List[str]) -> List[str]:
    """[Шаг 10] Сортировка по последнему символу"""
    return sorted(lst, key=lambda s: s[-1] if s else "")


def sort_numbers_squared(lst: List[int]) -> List[int]:
    """[Шаг 10] Сортировка чисел по квадрату. Внутри используется map()."""
    # создаём пары (orig, square) с помощью map
    mapped: List[Tuple[int, int]] = list(map(lambda x: (x, x * x), lst))
    mapped_sorted = sorted(mapped, key=lambda t: t[1])
    return [t[0] for t in mapped_sorted]


def sort_strings_upper(lst: List[str]) -> List[str]:
    """[Шаг 10] Сортировка строк по верхнему регистру. Внутри используется map()."""
    mapped: List[Tuple[str, str]] = list(map(lambda s: (s, s.upper()), lst))
    mapped_sorted = sorted(mapped, key=lambda t: t[1])
    return [t[0] for t in mapped_sorted]


def sort_abs(lst: List[int]) -> List[int]:
    """[Шаг 10] Сортировка чисел по модулю. Внутри используется map()."""
    mapped: List[Tuple[int, int]] = list(map(lambda x: (x, abs(x)), lst))
    mapped_sorted = sorted(mapped, key=lambda t: t[1])
    return [t[0] for t in mapped_sorted]


def sort_reverse_alpha(lst: List[str]) -> List[str]:
    """[Шаг 10] Сортировка строк в обратном алфавитном порядке"""
    return sorted(lst, reverse=True)


# ---------- Шаг 11 ----------

def pop_min(lst: List[int]) -> Optional[int]:
    """[Шаг 11] Извлекает и удаляет минимальный элемент (возвращает его либо None)."""
    if not lst:
        return None
    minimal_element = min(lst)
    lst.remove(minimal_element)
    return minimal_element


# ---------- КОРТЕЖИ ----------

# Шаг 12
def concat_tuples(*tuples: Tuple[Any, ...]) -> Tuple[Any, ...]:
    """[Шаг 12] Объединяет кортежи"""
    result: Tuple[Any, ...] = ()
    for element in tuples:
        result += element
    return result


def tuple_sum(tpl: Tuple[Any, ...]) -> float:
    """[Шаг 12] Суммирует числовые элементы кортежа"""
    return sum(x for x in tpl if isinstance(x, (int, float)))


# Шаг 13
def tuple_types(tpl: Tuple[Any, ...]) -> Tuple[type, ...]:
    """[Шаг 13] Возвращает кортеж типов элементов"""
    return tuple(type(x) for x in tpl)


# Шаг 14
def element_in_tuple(tpl: Tuple[Any, ...], element: Any) -> bool:
    """[Шаг 14] Проверяет, есть ли элемент в кортеже"""
    return element in tpl


# ---------- ДВУМЕРНЫЕ СПИСКИ ----------

# Шаг 15
def make_matrix_from_lists(*lists: List[Any]) -> List[List[Any]]:
    """[Шаг 15] Формирует двумерный список (матрицу) из переданных списков"""
    return [list(l) for l in lists]


# ---------- СЛОВАРИ ----------

# Шаг 16
def dict_keys(dct: Dict[Any, Any]) -> List[Any]:
    """[Шаг 16] Возвращает список ключей"""
    return list(dct.keys())


def dict_values(dct: Dict[Any, Any]) -> List[Any]:
    """[Шаг 16] Возвращает список значений"""
    return list(dct.values())


def dict_items(dct: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
    """[Шаг 16] Возвращает список пар (ключ, значение)"""
    return list(dct.items())


# Шаг 17
def count_key_occurrences(key: Any, *dicts: Dict[Any, Any]) -> int:
    """[Шаг 17] Считает, в скольких словарях встречается заданный ключ"""
    return sum(1 for d in dicts if key in d)


# Шаг 18
def find_nested_element(dct: Dict[Any, Any]) -> Optional[Any]:
    """[Шаг 18] Рекурсивно ищет все элементы, находящиеся на самом последнем уровне вложенности.
    Возвращает список значений с максимально глубокой вложенностью.
    """
    result: List[Any] = []
    max_depth = 0  # оборачиваем в список, чтобы изменять внутри вложенной функции

    def helper(current: Dict[str, Any], depth: int):
        nonlocal max_depth
        for value in current.values():
            if isinstance(value, dict):
                helper(value, depth + 1)
            else:
                if depth > max_depth:
                    max_depth = depth
                    result.clear()
                result.append(value)

    helper(dct, 1)
    return result


# ---------- ШАГ 19 ----------

def run_all() -> None:
    """[Шаг 19] Демонстрация всех функций (короткий пример использования)"""
    print("*** Шаг 1 ***", reverse_list([1, 2, 3]))
    print("*** Шаг 2 ***", modify_list([1, 2, 3], [1], 99))
    print("*** Шаг 3 ***", compare_lists([1, 2], [1, 2]))
    print("*** Шаг 4 ***", slice_list([1, 2, 3, 4, 5], 1, 4, 2))
    print("*** Шаг 5 ***", create_list_from_params(10, 20, 30))
    print("*** Шаг 6 ***", insert_element([1, 2, 3], 99, 1))
    print("*** Шаг 7 ***", merge_and_sort_lists([3, 1], [2, 4]))
    print("*** Шаг 8 ***", random_list_process())
    print("*** Шаг 9 ***", append_and_trim([1, 2], [3, 4, 5, 6], threshold=5))
    print("*** Шаг 10 ***")
    print(" sort_by_length:", sort_by_length(["apple", "kiwi", "banana"]))
    print(" sort_by_last_char:", sort_by_last_char(["cat", "dog", "bird"]))
    print(" sort_numbers_squared:", sort_numbers_squared([3, -2, 1]))
    print(" sort_strings_upper:", sort_strings_upper(["abc", "XYZ", "def"]))
    print(" sort_abs:", sort_abs([-5, 2, -3, 1]))
    print(" sort_reverse_alpha:", sort_reverse_alpha(["b", "a", "c"]))
    lst = [5, 1, 3]
    print("*** Шаг 11 ***", pop_min(lst), lst)
    print("*** Шаг 12 ***")
    print(" concat_tuples:", concat_tuples((1, 2), (3, 4)))
    print(" tuple_sum:", tuple_sum((1, 2, 3.5, "x")))
    print("*** Шаг 13 ***", tuple_types((1, "abc", 3.14)))
    print("*** Шаг 14 ***", element_in_tuple((1, 2, 3), 2))
    print("*** Шаг 15 ***", make_matrix_from_lists([1, 2], [3, 4]))
    dict_ = {"a": 1, "b": 2}
    print("*** Шаг 16 ***", dict_keys(dict_), dict_values(dict_), dict_items(dict_))
    dict_1, dict_2, dict_3 = {"name": "Ann"}, {"age": 20, "name": "Tom"}, {"age": 30}
    print("*** Шаг 17 ***", count_key_occurrences("name", dict_1, dict_2, dict_3))
    nested = {
        "lvl1": {
            "a": 1,
            "lvl2": {
                "b": 2,
                "c": 5,
                "lvl3": {
                    "x": 10,
                    "y": 20
                }
            }
        }
    }
    print("*** Шаг 18 ***", find_nested_element(nested))
