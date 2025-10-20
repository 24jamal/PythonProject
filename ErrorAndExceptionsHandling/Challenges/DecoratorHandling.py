

def decorator(funct):

    def wrapper():

        print("Before print")
        funct()
        print("After print")
    
    return wrapper

def greet():
    print("Hello world")

#without @decorator so we need to create a var to pass the greet function to decoreator function
var1 = decorator(greet)
var1()

#-----------------------------------------------------



def decorator1(funct):

    def wrapper():

        print("Before print")
        funct()
        print("After print")
    
    return wrapper

# with decorator calling
@decorator1
def greet():
    print("Hello world")

greet()