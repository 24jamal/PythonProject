def handling_exception(func):

    def wrapper(*args, **kwargs):

        try :

            return func(*args, **kwargs)
        except Exception as e:

            print(f"Exception in {func.__name__} function")
            print(e)
    return wrapper

@handling_exception
def divide(a,b):

    print(a/b)
    return a /b

@handling_exception
def read_file(filename):

    f = open(filename,'r')

    print(f.read())

divide(20,2)

read_file("ErrorAndExceptionsHandling/Challenges/data.txt")
