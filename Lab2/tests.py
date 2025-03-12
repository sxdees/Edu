import pytest
from lab2_bankapp import BankApp

@pytest.fixture
def setup_accounts():
    account1 = BankApp("Petr Ivanov", 15000)
    account2 = BankApp("Andrew Petrov", 8000)
    return account1, account2

def test_deposit(setup_accounts):
    account1, _ = setup_accounts
    account1.deposit(2500)
    assert account1.get_balance() == 17500
    with pytest.raises(ValueError, match="Deposit amount must be greater than zero."):
        account1.deposit(-500)

def test_withdraw(setup_accounts):
    account1, _ = setup_accounts
    account1.withdraw(4200)
    assert account1.get_balance() == 10800
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.withdraw(20000)

def test_transfer(setup_accounts):
    account1, account2 = setup_accounts
    account1.transfer(account2, 1500)
    assert account1.get_balance() == 13500
    assert account2.get_balance() == 9500
    with pytest.raises(ValueError, match="Insufficient funds."):
        account1.transfer(account2, 20000)

def test_invalid_target_account(setup_accounts):
    account1, _ = setup_accounts
    with pytest.raises(ValueError, match="Target account must be an instance of BankAccount."):
        account1.transfer("not a BankApp", 1000)
