"""
Основной модуль для демонстрации работы всех функций банковской системы.
Задание 9: Последовательный вызов всех функций
"""

from bank_operations import (
    validate_account_creation,
    calculate_interest,
    process_deposit,
    process_withdrawal,
    transfer_funds_with_exchange,
    process_investment_portfolio,
    analyze_credit_history,
    process_loan_application,
    close_bank_account,
    calculate_monthly_payment,
    validate_credit_card,
    process_bank_fee
)

from bank_exceptions import InsufficientFundsException, InvalidAmountException, AccountNotFoundException


def demonstrate_all_bank_operations():
    """
    Задание 9: Функция, которая последовательно вызывает ВСЕ вышесозданные функции.
    Завершается корректно без необработанных исключений.
    """
    print("*** ДЕМОНСТРАЦИЯ БАНКОВСКОЙ СИСТЕМЫ ***\n")

    account_balance = 1000.0
    account_id = "1234567890"

    try:
        # Задания 1: Функции без обработчиков исключений
        print("1. Функции без обработчиков исключений:")
        try:
            validate_account_creation(21, 500)
            print("   Создание счета: валидация пройдена")
        except ValueError as e:
            print(f"   Ошибка валидации: {e}")
        try:
            validate_account_creation(17, 500)
            print("   Создание счета: валидация пройдена")
        except ValueError as e:
            print(f"   Ошибка валидации: {e}")

        try:
            interest = calculate_interest(1000, 5, 3)
            print(f"   Расчет процентов: {interest:.2f}")
        except ValueError as e:
            print(f"   Ошибка расчета: {e}")
        try:
            interest = calculate_interest(1000, 5, 0)
            print(f"   Расчет процентов: {interest:.2f}")
        except ValueError as e:
            print(f"   Ошибка расчета: {e}")
        print()

        # Задания 2: Функция с одним обработчиком Exception без finally
        print("2. Обработка депозита:")
        account_balance = process_deposit(account_balance, 200)
        account_balance = process_deposit(account_balance, -100)
        print()

        # Задания 3: Функция с одним обработчиком Exception с finally
        print("3. Обработка снятия средств:")
        account_balance = process_withdrawal(account_balance, 300)
        account_balance = process_withdrawal(account_balance, 2000)
        print()

        # Задания 4: Функции с несколькими обработчиками разных типов исключений
        print("4.1. Перевод средств с конвертацией валют:")
        balance1, balance2 = transfer_funds_with_exchange(1000, 500, 200,
                                                          0.85, 'EUR')  # Успешно
        balance1, balance2 = transfer_funds_with_exchange(1000, 500,
                                                          200, 0, 'EUR')  # ZeroDivisionError
        balance1, balance2 = transfer_funds_with_exchange(1000, 500, "200",
                                                          0.85, 'EUR')  # TypeError
        balance1, balance2 = transfer_funds_with_exchange(1000, 500, 200,
                                                          0.85, 'JPY')  # ValueError
        print()

        print("4.2. Обработка инвестиционного портфеля:")
        portfolio = {
            'assets': [
                {'name': 'Акции', 'value': 50000},
                {'name': 'Облигации', 'value': 30000},
                {'name': 'Недвижимость', 'value': 20000}
            ],
            'total_value': 100000
        }
        result = process_investment_portfolio(portfolio,
                                              'moderate')  # Успешно

        # Тест с ошибками
        bad_portfolio = {'total_value': 100000}  # Нет ключа 'assets'
        result2 = process_investment_portfolio(bad_portfolio,
                                               'moderate')  # KeyError

        bad_portfolio2 = {
            'assets': [
                {'name': 'Акции', 'value': -10}  # Стоимость отрицательна
            ],
            'total_value': 100000
        }
        result3 = process_investment_portfolio(bad_portfolio2,
                                               'moderate')  # ArithmeticError
        print()

        print("4.3. Анализ кредитной истории:")
        credit_data = {
            'payments': [
                {'status': 'on_time'}, {'status': 'on_time'}, {'status': 'late'},
                {'status': 'on_time'}, {'status': 'missed'}, {'status': 'on_time'}
            ],
            'credit_cards': [{'limit': 100000}],
            'loans': [{'balance': 25000}]
        }
        credit_analysis = analyze_credit_history(credit_data, 6)  # Успешно

        # Тест с ошибками
        short_credit_data = {
            'payments': [{'status': 'on_time'}],  # Мало данных
            'credit_cards': [{'limit': 100000}],
            'loans': [{'balance': 25000}]
        }
        credit_analysis2 = analyze_credit_history(short_credit_data,
                                                  12)  # IndexError

        incomplete_data = {
            'payments': [{'status': 'on_time'}]
            # Нет credit_cards и loans
        }
        credit_analysis3 = analyze_credit_history(incomplete_data,
                                                  6)  # KeyError
        print()

        # Задания 5: Функция с генерацией исключений
        print("5. Обработка заявки на кредит:")
        loan_result = process_loan_application(30, 50000,
                                               720, 100000)
        print(f"   Результат: {loan_result}")
        print()

        # Задания 7: Функция с пользовательскими исключениями
        print("7. Закрытие банковского счета:")
        account_balance = close_bank_account(account_balance, account_id)
        print()

        # Задания 8: Дополнительные функции
        print("8.1. Расчет ежемесячного платежа:")
        payment = calculate_monthly_payment(100000, 8.5, 36)
        print(f"   Ежемесячный платеж: {payment}")
        print()

        print("8.2. Валидация кредитной карты:")
        is_card_valid = validate_credit_card("1234567812345678", "12/25", "123")
        print(f"   Карта валидна: {is_card_valid}")
        print()

        print("8.3. Обработка банковских комиссий:")
        account_balance = process_bank_fee(account_balance, "monthly")
        print()

        # Задания 6: Демонстрация пользовательских исключений
        print("6. Демонстрация пользовательских исключений:")
        try:
            raise InsufficientFundsException(100, 200)
        except InsufficientFundsException as e:
            print(f"   Поймано исключение: {e}")

        try:
            raise InvalidAmountException(-50)
        except InvalidAmountException as e:
            print(f"   Поймано исключение: {e}")

        try:
            raise AccountNotFoundException("invalid_id")
        except AccountNotFoundException as e:
            print(f"   Поймано исключение: {e}")

    except Exception as e:
        print(f"КРИТИЧЕСКАЯ ОШИБКА: {e}")

    print("\n*** ВСЕ ОПЕРАЦИИ УСПЕШНО ЗАВЕРШЕНЫ ***")
    return True


if __name__ == "__main__":
    demonstrate_all_bank_operations()
