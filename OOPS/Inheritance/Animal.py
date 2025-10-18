class Animal :

    def __init__(self ,name):

        self.name = name

    def speak(self):

        raise NotImplementedError(f"{self.name} speaks ")
    
class Dog(Animal):

    def speak(self):
        return self.name + "woofs"
    

class Cat(Animal):

    def speak(self):
        return self.name + "meows"
    

cat1 = Cat("kitty")
dog1 = Dog("Goldy")
    
print(cat1.speak())
print(dog1.speak())