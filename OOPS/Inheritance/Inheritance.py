class Animal:

    def __init__(self, name, age):

        self.name = name
        self.age = age

    
    def details(self):

        print(f"{self.name} {self.age}")

    
class Dog(Animal):

    def __init__(self, name, age, tails):
        super().__init__(name,age)
        self.tails = tails

    def details(self):
        print(f"Dog details :: {self.name} {self.age} {self.tails}")
dog1 = Dog("Jack",23,4)
dog1.details()

print(type(dog1))