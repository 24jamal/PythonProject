class AccountError(Exception):
    pass

class Account:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if (amount < 0):
            print("Enter the valid amount")
        else :
            self.balance = self.balance + amount
            print(f"Current Balance : {self.balance}")

    def withdrawal(self,amount):

        try: 
            if (amount > self.balance):
                print("Not suffient Funds")
                raise AccountError("Not sufficent balance :(")
            else :
                self.balance = self.balance - amount
                print(f"Current Balance : {self.balance}")
        
        except AccountError as e:
            print(e)

    def details(self):

        print(f"Name : {self.name} || Balance : {self.balance}")

def main():
    myacc = Account("jamal",1000)
    myacc.deposit(200)

    myacc.withdrawal(10000)
    myacc.withdrawal(300)

    myacc.details()

main()