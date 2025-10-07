# Содержит функции для шагов 4-7 и для шага 9.

import random
import math
import locale
from decimal import Decimal, getcontext

from data_classes import Book, Author, LibraryMember

# Шаг 4: Функции с использованием random
def generate_random_book_id():
    """Генерирует случайный ID книги с использованием методов random. (Шаг 4)"""
    return f"B{random.randint(1000, 9999)}-{random.choice(['A', 'B', 'C'])}"

def shuffle_book_list(books):
    """Перемешивает список книг с использованием random.shuffle. (Шаг 4)"""
    random.shuffle(books)
    return books

# Шаг 5: Функции с использованием math
def calculate_book_age(year):
    """Вычисляет возраст книги с использованием методов math. (Шаг 5)"""
    current_year = 2025  # Текущий год
    return math.floor(current_year - year)

def hypotenuse_example(a, b):
    """Использует math.hypot для вычисления гипотенузы. (Шаг 5)"""
    return math.hypot(a, b)

def log_book_count(count):
    """Использует math.log для логарифмического масштабирования количества книг. (Шаг 5)"""
    return math.log(count) if count > 0 else 0

# Шаг 6: Функции с использованием locale
def format_currency(amount):
    """Форматирует сумму как валюту с использованием locale. (Шаг 6)"""
    locale.setlocale(locale.LC_ALL, '')
    return locale.currency(amount, grouping=True)

def format_number(number):
    """Форматирует число с группировкой по locale. (Шаг 6)"""
    locale.setlocale(locale.LC_ALL, '')
    return locale.format_string("%d", number, grouping=True)

def parse_currency(string):
    """Разбирает строку валюты с использованием locale. (Шаг 6)"""
    locale.setlocale(locale.LC_ALL, '')
    return locale.atof(string.strip("$"))

# Шаг 7: Функции с использованием decimal
def precise_addition(a, b):
    """Точное сложение с использованием Decimal. (Шаг 7)"""
    getcontext().prec = 10
    return Decimal(a) + Decimal(b)

def precise_multiplication(a, b):
    """Точное умножение с использованием Decimal. (Шаг 7)"""
    getcontext().prec = 10
    return Decimal(a) * Decimal(b)

# Шаг 9: Функции с использованием data-классов
def process_book(book: Book):
    """Обрабатывает объект Book (передача как параметр). (Шаг 9.1)"""
    print(f"Обработка книги: {book.title} от {book.author}")

def handle_book_list(books: list[Book]):
    """Работает со списком объектов Book. (Шаг 9.2)"""
    return [book.title for book in books]

def manage_author_dict(authors: dict[str, Author]):
    """Работает со словарем, где значения — объекты Author. (Шаг 9.3)"""
    for key, author in authors.items():
        print(f"ID автора {key}: {author.name}")

def modify_member(member: LibraryMember):
    """Модифицирует значения объекта LibraryMember. (Шаг 9.4)"""
    member.name = member.name.upper()
    return member

def create_author_from_params(name: str, birth_year: int, nationality: str) -> Author:
    """Создает объект Author из параметров. (Шаг 9.5)"""
    return Author(name, birth_year, nationality)