from datetime import datetime
from typing import List
import re
from collections import Counter


# --------------------
# [Шаг 1]
# --------------------
def get_current_year() -> int:
    """Возвращает текущий год (вспомогательная функция для шага 1.)"""
    return datetime.now().year


def create_user_message(name: str, age: int, purchases: int) -> str:
    """Шаг 1.
    Формирует приветственное сообщение для пользователя. Вставляет:
      - строку (имя пользователя)
      - результат арифметической операции (возраст через 5 лет)
      - результат вызова функции (текущий год)
    """
    next_age = age + 5
    current_year = get_current_year()

    template = (f"Привет, {name}! Сейчас {current_year} год. "
                f"Через 5 лет тебе будет {next_age} лет, "
                f"а у тебя уже {purchases} покупок!")

    return template


# --------------------
# [Шаг 2]
# --------------------
def repeat_combination_lines(components: List[str], repeat_count: int, sep: str = " ") -> str:
    """
    Шаг 2.
    Формирует строку, состоящую из повторений комбинации других строк.
    - components: список строк, которые комбинируются в одну «фразу» через sep
    - repeat_count: сколько раз повторить эту фразу (целое >= 0)
    - sep: разделитель между компонентами внутри одной фразы (по умолчанию пробел)
    """
    if repeat_count <= 0:
        return ""

    phrase = sep.join(components)

    lines = [phrase for _ in range(repeat_count)]

    result = "\n".join(lines)
    return result


# --------------------
# [Шаг 3]
# --------------------
def count_substring_case_insensitive(text: str, substring: str) -> int:
    """
    Шаг 3.
    Считает количество вхождений подстроки в строке без учёта регистра.
    - text (str): исходная строка
    - substring (str): подстрока для поиска
    """
    lower_text = text.lower()
    lower_substring = substring.lower()

    return lower_text.count(lower_substring)


# --------------------
# [Шаг 4]
# --------------------
def substring_between_indices(s: str, start: int, end: int) -> str:
    """
    Шаг 4.
    Возвращает подстроку строки между двумя индексами.
    Тело функции реализовано в одну строку.
    Индексы должны быть больше 0 и меньше длины строки - 1.
    """
    return s[start:end] if 0 < start < len(s) - 1 and 0 < end <= len(s) - 1 and start < end else ""


# --------------------
# [Шаг 5]
# --------------------
def find_words_with_latin_letters(*strings: str):
    """
    Шаг 5.
    Принимает произвольное количество строк, содержащих кириллические и/или визуально схожие латинские буквы.
    Определяет слова, в которых встречаются латинские буквы.
    Возвращает кортеж:
        (список строк, где найдены латинские символы, количество таких слов)
    """

    # Регулярное выражение для поиска слов с латинскими буквами (a-zA-Z)
    latin_pattern = re.compile(r"[A-Za-z]")

    strings_with_latin = [s for s in strings if latin_pattern.search(s)]

    return strings_with_latin, len(strings_with_latin)


# --------------------
# [Шаг 6]
# --------------------
def is_palindrome(text: str) -> bool:
    """
    Шаг 6.
    Определяет, является ли строка палиндромом (одинаково читается с начала и конца).
    Игнорирует регистр и пробелы.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())

    return cleaned == cleaned[::-1]


# --------------------
# [Шаг 7]
# --------------------
def remove_extra_spaces_and_length(s: str) -> int:
    """
    Шаг 7.
    Убирает лишние пробелы: обрезает пробелы в начале/конце и сводит
    несколько пробельных символов между словами к одному пробелу.
    Возвращает длину строки после очистки.
    """
    cleaned = " ".join(s.split())
    return len(cleaned)


# --------------------
# [Шаг 8]
# --------------------
def split_sentences_to_lines(text: str) -> str:
    """
    Шаг 8.
    Принимает строку, содержащую несколько предложений.
    Заменяет знаки конца предложений (. ! ?) на символ переноса строки.
    Возвращает новую строку, где каждое предложение с новой строки.
    """
    # Убираем пробелы в начале и конце и заменяем все знаки конца предложений
    result = re.sub(r"[.!?]+\s*", "\n", text.strip())
    return result


# --------------------
# [Шаг 9]
# --------------------
def word_frequency(text: str) -> dict:
    """
    Шаг 9.1.
    Возвращает словарь: слово → количество повторений
    Приводит все слова к нижнему регистру
    """
    words = re.findall(r"\b\w+\b", text.lower())
    return dict(Counter(words))


def mask_email(email: str) -> str:
    """
    Шаг 9.2.
    Маскирует часть email перед @, оставляя первые и последние буквы
    """
    try:
        local, domain = email.split("@")
        if len(local) <= 2:
            masked_local = local[0] + "*"
        else:
            masked_local = local[0] + "*" * (len(local) - 2) + local[-1]
        return f"{masked_local}@{domain}"
    except Exception:
        return email  # если формат неверный, возвращаем как есть


def make_abbreviation(text: str) -> str:
    """
    Шаг 9.3.
    Берёт первую букву каждого слова и формирует аббревиатуру в верхнем регистре
    """
    words = re.findall(r"\b\w", text)
    return "".join(words).upper()
