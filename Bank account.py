# Class Client
class Client:
    def __init__(self, id, firstName, lastName):
        self.__id = id
        self.__firstName = firstName
        self.__lastName = lastName
        self.accounts = []  # List to hold multiple accounts

    def get_id(self): return self.__id
    def get_firstName(self): return self.__firstName
    def get_lastName(self): return self.__lastName

    def add_account(self, account):
        self.accounts.append(account)

# Class Account
class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def __init__(self, owner):
        Account.__nbAccounts += 1
        self.__code = Account.__nbAccounts
        self.__balance = 0.0
        self.__owner = owner
        self.history = []  # List to store history
        owner.add_account(self)  # Add this account to the owner's accounts

    # Access methods
    def get_code(self): return self.__code
    def get_balance(self): return self.__balance
    def get_owner(self): return self.__owner

    # Credit and debit methods
    def credit(self, amount, account=None):
        if account is None:
            self.__balance += amount
            self.history.append(f"Deposit: +{amount} DA")
        else:
            self.__balance += amount
            self.history.append(f"Transfer received: +{amount} DA from Account {account.get_code()}")
            account.debit(amount, self)

    def debit(self, amount, account=None):
        if self.__balance >= amount:
            self.__balance -= amount
            if account is not None:
                self.history.append(f"Transfer sent: -{amount} DA to Account {account.get_code()}")
                account.credit(amount, self)
            else:
                self.history.append(f"Withdraw: -{amount} DA")
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.__owner.get_firstName()} {self.__owner.get_lastName()} (ID: {self.__owner.get_id()})")
        print(f"Balance: {self.__balance} DA")
        print("History:")
        for entry in self.history:
            print("  ", entry)

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)
