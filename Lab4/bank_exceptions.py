"""
Пользовательские исключения для банковской системы.
Шаг 6: Пользовательские исключения
"""


class BankException(Exception):
    """Базовое исключение для банковской системы."""
    pass


class InsufficientFundsException(BankException):
    """Исключение при недостаточности средств на счете."""

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Недостаточно средств. Баланс: {balance}, требуется: {amount}")


class InvalidAmountException(BankException):
    """Исключение при невалидной сумме операций."""

    def __init__(self, amount):
        self.amount = amount
        super().__init__(f"Некорректная сумма: {amount}. Сумма должна быть положительной.")


class AccountNotFoundException(BankException):
    """Исключение при отсутствии счета."""

    def __init__(self, account_id):
        self.account_id = account_id
        super().__init__(f"Счет с ID {account_id} не найден.")
