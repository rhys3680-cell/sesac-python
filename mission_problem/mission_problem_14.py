class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def withdraw(self, amount):
        self.__balance -= amount
        print("통장에서 %d이 출금되었음" % (amount))
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print("통장에서 %d이 입금되었음" % (amount))
        return self.__balance
