class Circle:

    pi = 3.14
    def __init__(self, radius):

        self.radius = radius

    def area(self):

        print(f"Pi =  {self.pi}")
        print(f"Area : {self.pi * self.radius * self.radius}")

mycircle = Circle(3)
mycircle.area()



