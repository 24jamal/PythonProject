class Car():

    def __init__(self, brand, model, year):

        self.brand = brand
        self.model = model
        self.year = year

    def display(self):

        print(f"{self.brand} {self.model} {self.year}")

    def drive(self,speed):
        print(f"Car speed is  {speed}")

    def __str__(self):
        return f"{self.brand} -- {self.model}"
    
    def __len__(self):
        return self.year
    
car1 = Car("BMW","A1",2024)

car1.drive(200)

car1.display()

a = str(car1)

print(a)

print(len(car1))