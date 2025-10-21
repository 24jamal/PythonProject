def decorator(func):

    def wrapper(a,b):

        print("Before functions executes...")
        func(a,b)
        print("After functions executes...")

    return wrapper

@decorator
def sum(a,b):
    print(a+b)


sum(2,3)