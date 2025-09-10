from abc import ABC, abstractmethod   

class Account(ABC):
    def __init__(self, owner, balance=0):
        self.__owner = owner       
        self.__balance = balance

    @abstractmethod
    def account_type(self):
        """Each account must define its type"""
        pass

    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} deposited. New balance: {self.__balance}")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds!")

    def get_balance(self):
        return self.__balance

    def get_owner(self):
        return self.__owner
    
    def __str__(self):
        return f"{self.get_owner()} has {self.get_balance()} in their account."

class SavingsAccount(Account):
    def account_type(self):
        return "Savings Account"

class CurrentAccount(Account):
    def account_type(self):
        return "Current Account"

if __name__ == "__main__":

    acc1 = SavingsAccount("Berry", 1000)
    acc2 = CurrentAccount("Cherry", 500)

    print(f"{acc1.get_owner()} has {acc1.get_balance()} in {acc1.account_type()}")
    print(f"{acc2.get_owner()} has {acc2.get_balance()} in {acc2.account_type()}")

    for acc in (acc1, acc2):
        print(f"{acc.get_owner()} owns a {acc.account_type()}")

    acc1.deposit(500)
    acc1.withdraw(2000)  
    acc2.withdraw(200)

print(acc1)  
print(acc2)    
