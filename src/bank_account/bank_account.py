from dataclasses import dataclass, field
from typing import ClassVar, TypeVar

TBankAccount = TypeVar("TBankAccount", bound="BankAccount")


@dataclass
class BankAccount:
    next_id: ClassVar[int] = 1000
    accounts: ClassVar[list] = []
    balance: float = 0
    number: int = field(init=False)

    def __post_init__(self):
        if self.balance < 0:
            raise ValueError(f"Cannot open account with {self.balance} balance")
        self.number = BankAccount.next_id
        BankAccount.next_id += 1
        BankAccount.accounts.append(self)

    def deposit(self, amount: float):
        if amount < 0:
            raise ValueError(f"Cannot deposit {amount}")
        self.balance += amount

    def withdraw(self, amount: float):
        if amount < 0:
            raise ValueError(f"Can't withdraw {amount}")
        if self.balance - amount < 0:
            raise ValueError(f"Can't withdraw {amount} with {self.balance} balance")
        self.balance -= amount

    def transfer(self, other: TBankAccount, amount: float):
        self.withdraw(amount)
        other.deposit(amount)

    # def __repr__(self):
    #     return f"{type(self).__name__}({self.balance})"


def test_equal(res, expected_res):
    assert res == expected_res, f"Wrong result, got:\n\t{res}\nbut expected\n\t {expected_res}"


def main():
    # Base exercise:
    account1 = BankAccount()
    test_equal(account1.balance, 0)
    account1.deposit(10)
    test_equal(account1.balance, 10)
    account2 = BankAccount(balance=20)
    account2.withdraw(15)
    test_equal(account2.balance, 5)
    account1.transfer(account2, 3)
    test_equal(account1.balance, 7)
    test_equal(account2.balance, 8)

    # Bonus 1
    try:
        account1 = BankAccount(-10)
        raise Exception("Should have raised a ValueError but did not.")
    except ValueError as error:
        test_equal(str(error), "Cannot open account with -10 balance")
        pass
    account1 = BankAccount(balance=10)
    try:
        account1.withdraw(-5)
        raise Exception("Should have raised a ValueError but did not.")
    except ValueError as error:
        test_equal(str(error), "Can't withdraw -5")
        pass
    try:
        account1.withdraw(50)
        raise Exception("Should have raised a ValueError but did not.")
    except ValueError as error:
        test_equal(str(error), "Can't withdraw 50 with 10 balance")
        pass
    try:
        account1.deposit(-5)
        raise Exception("Should have raised a ValueError but did not.")
    except ValueError as error:
        test_equal(str(error), "Cannot deposit -5")
        pass
    account2 = BankAccount(balance=20)
    try:
        account1.transfer(account2, 100)
        raise Exception("Should have raised a ValueError but did not.")
    except ValueError as error:
        test_equal(str(error), "Can't withdraw 100 with 10 balance")
        pass

    # Bonus 2
    account1 = BankAccount(100)
    account2 = BankAccount()
    test_equal(account1.number, 1004)
    test_equal(account2.number, 1005)
    account3 = BankAccount(50)
    test_equal(account3.number, 1006)
    print("Passed tests!")


if __name__ == "__main__":
    main()
