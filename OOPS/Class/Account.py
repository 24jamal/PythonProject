class Account:

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):

        if (amount < 0):
            print("Enter the valid number")
        else:
            self.balance = self.balance + amount

    def withdrawal(self,amount):

        if (self.balance < amount):
            print("Not Enough funds in Account")
        else:
            self.balance = self.balance - amount

    def __str__(self):

        return f"{self.owner} : Available Balance : {self.balance}"


acc1 = Account("Jamal",1200)

print(str(acc1))

acc1.withdrawal(500)

acc1.deposit(101)


print(str(acc1))

