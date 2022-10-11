import datetime
import pytest
# BankAccount class definition
class BankAccount:
    def __init__(self, name: str = 'Rumbi Gwanz', ID: int = 123,
                 creation_date: datetime.date = datetime.date.today(),
                 balance: float = 0.0):
        self.name = name
        self.ID = ID
        self.creation_date = creation_date
        self.balance = balance

        if not isinstance(creation_date, datetime.date):
            raise Exception('Creation_date is not of type datetime.date')

        if creation_date > datetime.date.today():
            raise Exception('Creation_date is in the future.')

# method for deposit amount
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount cannot be zero or negative.")
        self.balance += amount

# method to withdraw amount
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount cannot be zero or negative.")
# getter method to return balance
    def view_balance(self):
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
        super().__init__(name, ID, creation_date, balance)

    # method to deposit amount
    def deposit(self, amount):
        return super().deposit(amount)

    # method to withdraw amount
    def withdraw(self, amount):
        super().withdraw(amount)
        if amount > self.balance:
            self.balance -= amount + 30
        else:
            self.balance -= amount

# get the method return balance
    def view_balance(self):
        return super().view_balance()


class SavingsAccount(BankAccount):
    def __init__(self, name, ID, creation_date, balance):
        super().__init__(name, ID, creation_date, balance)

# method to deposit amount
    def deposit(self, amount):
        return super().deposit(amount)

 # method to withdraw amount
    def withdraw(self, amount):
        super().withdraw(amount)
        if (datetime.date.today() - self.creation_date).days <= 180:
            raise ValueError("Account creation date is less than 6 months from today. "
                             "Withdrawals are only allowed after 6 months has passed since the creation of the account.")
        if amount > self.balance:
            raise ValueError('Insufficient balance.')
        self.balance -= amount

    # getter method to return balance
    def view_balance(self):
        return super().view_balance()


def test_constructor():
    with pytest.raises(Exception) as exc_info:
        BankAccount('richard', 456, str(datetime.date.today()), 2000)
    assert str(exc_info.value) == 'Creation_date is not of type datetime.date'
    with pytest.raises(Exception) as exc_info:
        BankAccount('richard', 456,  datetime.date.today() + datetime.timedelta(days=10), 2000)
    assert str(exc_info.value) == 'Creation_date is in the future.'


def test_savings_update():
    savings_bank_account = SavingsAccount('richard', 456, datetime.date.today() + datetime.timedelta(days=-300), 2000)
    savings_bank_account.withdraw(1000)
    assert savings_bank_account.view_balance() == 1000


def test_savings_negative():
    with pytest.raises(ValueError) as exc_info:
        savings_bank_account = SavingsAccount('richard', 456, datetime.date.today() + datetime.timedelta(days=-300),
                                              2000)
        savings_bank_account.withdraw(2200)
    assert str(exc_info.value) == 'Insufficient balance.'


def test_savings_young_account():
    with pytest.raises(ValueError) as exc_info:
        savings_bank_account = SavingsAccount('richard', 456, datetime.date.today() + datetime.timedelta(days=-100),
                                              2000)
        savings_bank_account.withdraw(200)
    assert str(exc_info.value) == 'Account creation date is less than 6 months from today. ' \
                                  'Withdrawals are only allowed after 6 months has passed since the creation of the account.'


@pytest.mark.xfail
def test_checking_deposit(checking_bank_account):
    checking_bank_account=CheckingAccount('richard', 456, datetime.date.today() + datetime.timedelta(days=-10), 2000)
    checking_bank_account.deposit(-200)
    assert checking_bank_account.view_balance() == 2000


def test_checking_withdraw():
    checking_bank_account = CheckingAccount('richard', 456,  datetime.date.today() + datetime.timedelta(days=-10), 2000)
    checking_bank_account.withdraw(1000)
    assert checking_bank_account.view_balance() == 1000


def test_checking_overdraft():
    checking_bank_account = CheckingAccount('richard', 456,  datetime.date.today() + datetime.timedelta(days=-10), 2000)
    checking_bank_account.withdraw(2100)
    assert checking_bank_account.view_balance() == -130
