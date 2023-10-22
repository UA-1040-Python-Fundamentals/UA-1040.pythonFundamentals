# Create a class "BankAccount" that implements encapsulation. The class should have the following
# attributes:
# account_number (string)
# account_holder (string)
# balance (float)
# The class should have the following methods:
# deposit(amount) - a method that allows the account holder to deposit money into the account
# withdraw(amount) - a method that allows the account holder to withdraw money from the account;
# write "Insufficient funds" if money doesn't enough
# check_balance() - a method that returns the current balance of the account
# The class should also have the following restrictions:
# account_number should not be accessible from outside the class
# balance should not be directly accessible from outside the class,
# it should only be accessible through the methods deposit() and withdraw()
# account_holder should be accessible from outside the class but should not be modifiable

class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = str(account_number)
        self.__account_holder = str(account_holder)
        self.__balance = float(balance)

    def deposit(self, amount):
        """The method that allows the account holder to deposit money into the account"""
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        """The method that allows the account holder to withdraw money from the account"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        """The method that returns the current balance of the account"""
        return self.__balance

    def get_account_holder(self):
        return self.__account_holder

    @property
    def account_holder(self):
        return self.__account_holder


my_account = BankAccount("123456789", "John Doe", 1000.0)
print(my_account.account_holder)

try:
    _ = my_account.account_number
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

try:
    _ = my_account.balance
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

print(my_account.check_balance())

my_account.deposit(500.0)
print(my_account.check_balance())

my_account.withdraw(250.0)
print(my_account.check_balance())

try:
    my_account.account_holder = "Jane Doe"
    print("Should have raised AttributeError")
except AttributeError:
    print("AttributeError raised as expected")

my_account.withdraw(5000.0)
