from datetime import datetime
from CustomError import (NonActiveAccountError, MaxAccountsError, NegativeBalanceError, InsufficientFundsError,
                         EmptyNameError, EmptyEmailError, InvalidDepositError, InvalidWithdrawalError)

class BankAccount:
    max_balance: float = 0
    min_balance: float = float('inf')
    balance_all_accounts: float = 0
    last_operation_time: datetime = None
    total_accounts = 0
    max_accounts = 10
    _all_accounts = [] # Store all created accounts

    def __init__(self, name: str, email: str, balance: float):
        if balance < 0:
            raise NegativeBalanceError()
        if BankAccount.total_accounts >= BankAccount.max_accounts:
            raise MaxAccountsError()

        self.name = name
        self.email = email
        self.__balance = 0
        self.balance = balance
        self.__active = True
        self.__last_operation_time = datetime.now()

        BankAccount._all_accounts.append(self)  # Track all instances

        BankAccount._increment_total_accounts()

    @classmethod
    def _get_all_accounts(cls):
        return [acc for acc in cls._all_accounts if acc.active]

    @classmethod
    def _increment_total_accounts(cls):
        cls.total_accounts += 1

    @classmethod
    def _update_balances(cls, old_balance, new_balance):
        """Efficiently updates balances only when necessary."""
        cls.balance_all_accounts += new_balance - old_balance

        if new_balance < cls.min_balance:
            cls.min_balance = new_balance
        elif new_balance > cls.max_balance:
            cls.max_balance = new_balance
        else:
            active_accounts = cls._get_all_accounts()
            cls.min_balance = min((acc.__balance for acc in active_accounts), default=float('inf'))
            cls.max_balance = max((acc.__balance for acc in active_accounts), default=0)

    @classmethod
    def _decrement_total_accounts(cls):
        cls.total_accounts -= 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise EmptyNameError()
        self.__name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if not value:
            raise EmptyEmailError()
        self.__email = value

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise NegativeBalanceError()
        old_balance = self.__balance
        self.__balance = value
        BankAccount._update_balances(old_balance, value)

    @property
    def active(self):
        return self.__active

    def deposit(self, amount: float):
        if not self.__active:
            raise NonActiveAccountError()
        if amount <= 0:
            raise InvalidDepositError()

        old_balance = self.__balance
        self.__balance += amount
        BankAccount._update_balances(old_balance, self.__balance)
        self.__last_operation_time = datetime.now()

    def withdraw(self, amount: float):
        if not self.__active:
            raise NonActiveAccountError()
        if amount <= 0:
            raise InvalidWithdrawalError()
        if amount > self.__balance:
            raise InsufficientFundsError()

        old_balance = self.__balance
        self.__balance -= amount
        BankAccount._update_balances(old_balance, self.__balance)
        self.__last_operation_time = datetime.now()


    def close_account(self):
        if not self.__active:
            raise NonActiveAccountError()

        self.__active = False
        old_balance = self.__balance
        self.__balance = 0
        BankAccount.balance_all_accounts -= old_balance
        BankAccount._decrement_total_accounts()

        # Ensure min/max balance is recalculated correctly after closing
        active_accounts = BankAccount._get_all_accounts()
        BankAccount.min_balance = min((acc.__balance for acc in active_accounts), default=float('inf'))
        BankAccount.max_balance = max((acc.__balance for acc in active_accounts), default=0)

        self.__last_operation_time = datetime.now()


    def __str__(self):
        return (f"Name: {self.__name}, Email: {self.__email}, Balance: {self.__balance}, "
                f"Active: {self.__active}, Last Operation: {self.__last_operation_time})")


    def __repr__(self):
        return f"BankAccount('{self.__name}', '{self.__email}', {self.__balance})"



