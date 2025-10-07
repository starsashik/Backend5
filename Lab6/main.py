# Содержит главную функцию согласно шагу 10.

import my_utilities
import demo_imports
from data_classes import Book, Author, LibraryMember


def main_demo():
    """Вызывает все функции из шагов 2-9. (Шаг 10)"""
    # Шаг 2: Демонстрация импортов
    print("*** Шаг 2 ***")
    demo_imports.demonstrate_imports()

    # Шаг 4: Функции с random
    print("*** Шаг 4 ***")
    print(my_utilities.generate_random_book_id())
    books = [Book("Книга1", "Автор1", 2000, "ISBN1"), Book("Книга2", "Автор2", 2010, "ISBN2")]
    print(my_utilities.shuffle_book_list(books))

    # Шаг 5: Функции с math
    print("*** Шаг 5 ***")
    print(my_utilities.calculate_book_age(2000))
    print(my_utilities.hypotenuse_example(3, 4))
    print(my_utilities.log_book_count(100))

    # Шаг 6: Функции с locale
    print("*** Шаг 6 ***")
    print(my_utilities.format_currency(1234.56))
    print(my_utilities.format_number(1000000))
    print(my_utilities.parse_currency("$1,234.56"))

    # Шаг 7: Функции с decimal
    print("*** Шаг 8 ***")
    print(my_utilities.precise_addition(0.1, 0.2))
    print(my_utilities.precise_multiplication(0.2, 2))

    # Шаг 9: Функции с data-классами
    print("*** Шаг 9 ***")
    book = Book("Программирование на Python", "Гвидо ван Россум", 1991, "ISBN123")
    my_utilities.process_book(book)
    book_list = [book, Book("Другая книга", "Автор", 2005, "ISBN456")]
    print(my_utilities.handle_book_list(book_list))
    author_dict = {"A1": Author("Автор1", 1950, "Голландец")}
    my_utilities.manage_author_dict(author_dict)
    member = LibraryMember("Иван Иванов", "M001")
    print(my_utilities.modify_member(member))
    new_author = my_utilities.create_author_from_params("Новый Автор", 1980, "Американец")
    print(new_author)


if __name__ == "__main__":
    main_demo()
