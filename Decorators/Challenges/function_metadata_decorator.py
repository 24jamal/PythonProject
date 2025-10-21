from functools import wraps

def annouce(message):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            print(f"INFO : {message}")
            return func(*args, **kwargs)
        
        return wrapper
    return decorator

@annouce("Subration method is used")
def subtration(a,b):

    """This function is used for subration operation"""
    return a-b

@annouce("Addition method is used")
def addition(a,b):
    """This function is used for addition operation"""
    return a+b

print(subtration(4,2))

print(subtration.__name__)
print(subtration.__doc__)

print(addition(2,8))
print(addition.__name__)
print(addition.__doc__)
