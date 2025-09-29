"""
Функции для работы с банковской системой.
Задания 1-5, 7-8: Различные типы обработки исключений
"""

from bank_exceptions import *


# Задания 1: Функции без обработчиков исключений (2 функции)
def validate_account_creation(age: int, initial_deposit: float) -> bool:
    """
    Задания 1: Валидация создания счета без обработки исключений.
    Выбрасывает ValueError при некорректных параметрах.
    """
    if age < 18:
        raise ValueError("Для создания счета необходимо быть старше 18 лет")
    if initial_deposit < 0:
        raise ValueError("Начальный депозит не может быть отрицательным")
    return True


def calculate_interest(principal: float, rate: float, years: int) -> float:
    """
    Задания 1: Расчет сложных процентов без обработки исключений.
    Выбрасывает TypeError и ValueError при некорректных параметрах.
    """
    if years <= 0:
        raise ValueError("Срок вклада должен быть положительным")
    if rate < 0:
        raise ValueError("Процентная ставка не может быть отрицательной")
    return principal * (1 + rate / 100) ** years


# Задания 2: Функция с одним обработчиком Exception без finally
def process_deposit(account_balance: float, deposit_amount: float) -> float:
    """
    Задания 2: Обработка депозита с одним обработчиком Exception.
    """
    try:
        if deposit_amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной")
        if deposit_amount > 1000000:
            raise ValueError("Сумма депозита превышает лимит в 1,000,000")

        new_balance = account_balance + deposit_amount
        print(f"Депозит успешно обработан. Новый баланс: {new_balance}")
        return new_balance

    except Exception as e:
        print(f"Ошибка при обработке депозита: {e}")
        # Логика обработки: возвращаем исходный баланс
        return account_balance


# Задания 3: Функция с одним обработчиком Exception с finally
def process_withdrawal(account_balance: float, withdrawal_amount: float) -> float:
    """
    Задания 3: Обработка снятия средств с блоком finally.
    """
    try:
        if withdrawal_amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if withdrawal_amount > account_balance:
            raise ValueError(f"Недостаточно средств. Баланс: {account_balance}, требуется: {withdrawal_amount}")

        new_balance = account_balance - withdrawal_amount
        print(f"Снятие успешно обработано. Новый баланс: {new_balance}")
        return new_balance

    except Exception as e:
        print(f"Ошибка при снятии средств: {e}")
        return account_balance

    finally:
        print("Операция снятия средств завершена (успешно или с ошибкой)")


# Задания 4: Функции с несколькими обработчиками разных типов исключений (3 функции)
def transfer_funds_with_exchange(from_balance: float, to_balance: float, amount: float,
                                 exchange_rate: float, currency: str) -> tuple:
    """
    Задания 4: Перевод средств с конвертацией валют с обработкой разных исключений.
    Обрабатывает: ValueError, TypeError, ZeroDivisionError
    """
    try:
        if currency not in ['USD', 'EUR', 'GBP']:
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

        if exchange_rate <= 0:
            raise ZeroDivisionError("Курс обмена должен быть положительным")

        if not isinstance(amount, (int, float)):
            raise TypeError(f"Сумма должна быть числом, получено: {type(amount)}")

        if amount <= 0:
            raise ValueError("Сумма перевода должна быть положительной")

        if amount > from_balance:
            raise ValueError(f"Недостаточно средств. Баланс: {from_balance}, требуется: {amount}")

        # Конвертация суммы
        converted_amount = amount / exchange_rate

        new_from_balance = from_balance - amount
        new_to_balance = to_balance + converted_amount

        print(f"Перевод успешен: {amount} руб. -> {converted_amount:.2f} {currency}")
        return new_from_balance, new_to_balance

    except ValueError as e:
        print(f"Ошибка валидации данных: {e}")
        return from_balance, to_balance

    except TypeError as e:
        print(f"Ошибка типа данных: {e}")
        return from_balance, to_balance

    except ZeroDivisionError as e:
        print(f"Ошибка вычислений: {e}")
        return from_balance, to_balance

    finally:
        print("Операция перевода с конвертацией завершена")


def process_investment_portfolio(portfolio: dict, risk_tolerance: str) -> dict:
    """
    Задания 4: Обработка инвестиционного портфеля с обработкой разных исключений.
    Обрабатывает: KeyError, ValueError, ZeroDivisionError, ArithmeticError
    """
    try:
        if 'assets' not in portfolio:
            raise KeyError("Отсутствует ключ 'assets' в портфеле")

        if 'total_value' not in portfolio:
            raise KeyError("Отсутствует ключ 'total_value' в портфеле")

        valid_risks = ['conservative', 'moderate', 'aggressive']
        if risk_tolerance not in valid_risks:
            raise ValueError(f"Недопустимый уровень риска. Допустимо: {valid_risks}")

        assets = portfolio['assets']
        total_value = portfolio['total_value']

        allocation = {}
        for asset in assets:
            if 'name' not in asset or 'value' not in asset:
                raise KeyError("Актив должен содержать 'name' и 'value'")

            if asset['value'] < 0:
                raise ArithmeticError("Стоимость актива не может быть отрицательной")

            if total_value == 0:
                raise ZeroDivisionError("Общая стоимость портфеля не может быть нулевой")

            percentage = (asset['value'] / total_value) * 100
            allocation[asset['name']] = round(percentage, 2)

        risk_multipliers = {
            'conservative': 0.6,
            'moderate': 1.0,
            'aggressive': 1.4
        }

        multiplier = risk_multipliers[risk_tolerance]
        recommended_allocation = {k: v * multiplier for k, v in allocation.items()}

        result = {
            'current_allocation': allocation,
            'recommended_allocation': recommended_allocation,
            'risk_tolerance': risk_tolerance
        }

        print(f"Портфель обработан для уровня риска: {risk_tolerance}")
        return result

    except KeyError as e:
        print(f"Ошибка структуры данных портфеля: {e}")
        return {'error': 'Неверная структура портфеля'}

    except (ValueError, ArithmeticError, ZeroDivisionError) as e:
        print(f"Ошибка вычислений или валидации: {e}")
        return {'error': 'Ошибка в расчетах портфеля'}

    finally:
        print("Анализ инвестиционного портфеля завершен")


def analyze_credit_history(credit_data: dict, months: int) -> dict:
    """
    Задания 4: Анализ кредитной истории с обработкой разных исключений.
    Обрабатывает: KeyError, IndexError, ZeroDivisionError, RuntimeError, MemoryError (имитация)
    """
    try:
        if 'payments' not in credit_data:
            raise KeyError("Отсутствуют данные о платежах")

        if 'credit_cards' not in credit_data:
            raise KeyError("Отсутствуют данные о кредитных картах")

        if 'loans' not in credit_data:
            raise KeyError("Отсутствуют данные о кредитах")

        payments = credit_data['payments']
        credit_cards = credit_data['credit_cards']
        loans = credit_data['loans']

        if len(payments) < months:
            raise IndexError(f"Недостаточно данных платежей. Имеется: {len(payments)}, требуется: {months}")

        recent_payments = payments[-months:]

        if None in recent_payments:
            raise ValueError("Обнаружены пропущенные данные о платежах")

        # Имитация возможной ошибки выполнения (например, при большом объеме данных)
        if len(payments) > 10000:
            raise MemoryError("Слишком большой объем данных для анализа")

        on_time_payments = sum(1 for payment in recent_payments if payment['status'] == 'on_time')
        late_payments = sum(1 for payment in recent_payments if payment['status'] == 'late')
        missed_payments = sum(1 for payment in recent_payments if payment['status'] == 'missed')

        if len(recent_payments) == 0:
            raise ZeroDivisionError("Нет данных о платежах для анализа")

        payment_ratio = on_time_payments / len(recent_payments)

        total_credit_limit = sum(card['limit'] for card in credit_cards)
        total_loan_balance = sum(loan['balance'] for loan in loans)

        if total_credit_limit == 0:
            raise ZeroDivisionError("Общий кредитный лимит не может быть нулевым")

        credit_utilization = total_loan_balance / total_credit_limit

        if payment_ratio >= 0.95 and credit_utilization <= 0.3:
            rating = "Отличный"
        elif payment_ratio >= 0.85 and credit_utilization <= 0.5:
            rating = "Хороший"
        elif payment_ratio >= 0.7:
            rating = "Удовлетворительный"
        else:
            rating = "Плохой"

        result = {
            'payment_ratio': round(payment_ratio, 3),
            'on_time_payments': on_time_payments,
            'late_payments': late_payments,
            'missed_payments': missed_payments,
            'credit_utilization': round(credit_utilization, 3),
            'credit_rating': rating,
            'analysis_period': f"{months} месяцев"
        }

        print(f"Анализ кредитной истории завершен. Рейтинг: {rating}")
        return result

    except KeyError as e:
        print(f"Ошибка отсутствующих данных: {e}")
        return {'error': 'Неполные данные кредитной истории'}

    except IndexError as e:
        print(f"Ошибка индексации данных: {e}")
        return {'error': 'Недостаточно данных для анализа'}

    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка валидации или вычислений: {e}")
        return {'error': 'Ошибка в данных кредитной истории'}

    except (MemoryError, RuntimeError) as e:
        print(f"Системная ошибка при анализе: {e}")
        return {'error': 'Проблема с обработкой данных'}

    finally:
        print("Анализ кредитной истории завершен")


# Задания 5: Функция с генерацией исключений и их обработкой
def process_loan_application(age: int, income: float, credit_score: int, loan_amount: float) -> dict:
    """
    Задания 5: Обработка заявки на кредит с генерацией исключений.
    """
    try:
        # Генерация исключений при определенных условиях
        if age < 21:
            raise ValueError("Заявитель должен быть старше 21 года")

        if age > 70:
            raise ValueError("Заявитель должен быть младше 70 лет")

        if income <= 0:
            raise ValueError("Доход должен быть положительным")

        if credit_score < 300 or credit_score > 850:
            raise ValueError("Кредитный рейтинг должен быть в диапазоне 300-850")

        if loan_amount <= 0:
            raise ValueError(f"Сумма кредита должна быть положительной: {loan_amount}")

        max_loan_amount = income * 5
        if loan_amount > max_loan_amount:
            raise ValueError(f"Сумма кредита превышает максимально допустимую: {max_loan_amount}")

        approval = credit_score >= 650 and loan_amount <= income * 3
        interest_rate = 8.5 if credit_score >= 750 else 12.0 if credit_score >= 650 else 15.5

        result = {
            'approved': approval,
            'interest_rate': interest_rate,
            'max_loan_amount': min(loan_amount, max_loan_amount)
        }

        print(f"Заявка на кредит обработана: {result}")
        return result

    except ValueError as e:
        print(f"Ошибка при обработке заявки на кредит: {e}")
        return {'approved': False, 'error': str(e)}

    except Exception as e:
        print(f"Неожиданная ошибка при обработке кредита: {e}")
        return {'approved': False, 'error': 'Внутренняя ошибка системы'}

    finally:
        print("Обработка заявки на кредит завершена")


# Задания 7: Функция с пользовательскими исключениями
def close_bank_account(account_balance: float, account_id: str) -> float:
    """
    Задания 7: Закрытие банковского счета с пользовательскими исключениями.
    """
    try:
        if account_balance < 0:
            raise InsufficientFundsException(account_balance, 0)

        if not account_id or len(account_id) != 10:
            raise AccountNotFoundException(account_id)

        if account_balance > 0:
            print(f"Счет {account_id} закрыт. Возвращено средств: {account_balance}")
        else:
            print(f"Счет {account_id} закрыт")

        return 0.0

    except (InsufficientFundsException, AccountNotFoundException) as e:
        print(f"Ошибка при закрытии счета: {e}")
        return account_balance

    finally:
        print(f"Операция закрытия счета {account_id} завершена")


# Задания 8: Дополнительные функции, демонстрирующие работу исключений (3 функции)
def calculate_monthly_payment(loan_amount: float, annual_rate: float, months: int) -> float:
    """
    Задания 8: Расчет ежемесячного платежа по кредиту.
    """
    try:
        if loan_amount <= 0:
            raise InvalidAmountException(loan_amount)
        if annual_rate <= 0:
            raise ValueError("Процентная ставка должна быть положительной")
        if months <= 0:
            raise ValueError("Срок кредита должен быть положительным")

        monthly_rate = annual_rate / 100 / 12
        payment = loan_amount * monthly_rate * (1 + monthly_rate) ** months / ((1 + monthly_rate) ** months - 1)

        print(f"Ежемесячный платеж: {payment:.2f}")
        return round(payment, 2)

    except (InvalidAmountException, ValueError) as e:
        print(f"Ошибка расчета платежа: {e}")
        return 0.0


def validate_credit_card(number: str, expiry_date: str, cvv: str) -> bool:
    """
    Задания 8: Валидация данных кредитной карты.
    """
    try:
        if not number or len(number) != 16 or not number.isdigit():
            raise ValueError("Номер карты должен содержать 16 цифр")

        if not expiry_date or '/' not in expiry_date:
            raise ValueError("Неверный формат даты истечения (MM/YY)")

        if not cvv or len(cvv) != 3 or not cvv.isdigit():
            raise ValueError("CVV должен содержать 3 цифры")

        month, year = expiry_date.split('/')
        if not month.isdigit() or not year.isdigit():
            raise ValueError("Месяц и год должны быть числами")

        print("Данные карты валидны")
        return True

    except ValueError as e:
        print(f"Ошибка валидации карты: {e}")
        return False


def process_bank_fee(account_balance: float, fee_type: str, amount: float = None) -> float:
    """
    Задания 8: Обработка банковских комиссий.
    """
    try:
        fees = {
            'monthly': 50.0,
            'overdraft': 100.0,
            'wire_transfer': 25.0
        }

        if fee_type not in fees:
            raise ValueError(f"Неизвестный тип комиссии: {fee_type}")

        fee_amount = amount if amount is not None else fees[fee_type]

        if fee_amount <= 0:
            raise InvalidAmountException(fee_amount)

        if account_balance < fee_amount:
            raise InsufficientFundsException(account_balance, fee_amount)

        new_balance = account_balance - fee_amount
        print(f"Комиссия '{fee_type}' списана: {fee_amount}. Новый баланс: {new_balance}")
        return new_balance

    except (ValueError, InvalidAmountException, InsufficientFundsException) as e:
        print(f"Ошибка при списании комиссии: {e}")
        return account_balance
