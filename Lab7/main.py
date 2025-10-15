from string_utils import (
    create_user_message,
    repeat_combination_lines,
    count_substring_case_insensitive,
    substring_between_indices,
    find_words_with_latin_letters,
    is_palindrome,
    remove_extra_spaces_and_length,
    split_sentences_to_lines,
    word_frequency,
    mask_email,
    make_abbreviation
)


def run_all_string_functions():
    """Шаг 10.
    Вызывает все функции шагов 1–9
    """
    try:
        print("=== Шаг 1 ===")
        msg = create_user_message("Иван", 25, 10)
        print(msg)

        print("\n=== Шаг 2 ===")
        repeated = repeat_combination_lines(["Супер", "скидка", "50%"], 3)
        print(repeated)

        print("\n=== Шаг 3 ===")
        text3 = "Hello hello HELLO world"
        count = count_substring_case_insensitive(text3, "hello")
        print(f"Количество вхождений 'hello': {count}")

        print("\n=== Шаг 4 ===")
        s4 = "Программирование"
        print(substring_between_indices(s4, 2, 7))

        print("\n=== Шаг 5 ===")
        suspicious, total = find_words_with_latin_letters("Привет", "Cамолет", "МОСКВА", "Реsume")
        print(f"Найдены слова: {suspicious}, количество: {total}")

        print("\n=== Шаг 6 ===")
        print(f"'А роза упала на лапу Азора' → {is_palindrome('А роза упала на лапу Азора')}")

        print("\n=== Шаг 7 ===")
        s7 = "   Это   пример   с   лишними   пробелами   "
        print(f"Длина строки после очистки: {remove_extra_spaces_and_length(s7)}")

        print("\n=== Шаг 8 ===")
        text8 = "Привет! Как дела? Всё хорошо."
        print(split_sentences_to_lines(text8))

        print("\n=== Шаг 9.1 ===")
        text9 = "Python это язык программирования. Python удобен!"
        print(word_frequency(text9))

        print("\n=== Шаг 9.2 ===")
        print(mask_email("Alexander@example.com"))

        print("\n=== Шаг 9.3 ===")
        print(make_abbreviation("Национальная служба безопасности"))

        print("\n=== Все функции выполнены успешно ===")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    run_all_string_functions()
