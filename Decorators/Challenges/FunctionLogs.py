import logging

logging.basicConfig(
    filename= "Decorators/Challenges/function_logs.txt",
    level= logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s "
)


def decorator(func):

    logging.debug("Inside Decorator Function")
    def wrapper(*args,**kwargs):
        logging.debug("Inside Wrapper Function")
        a = args
        b = kwargs
        print(a,b)
        logging.info(f"Arguments : {a} || Key words arguments : {b} ")
        logging.debug("End of Wrapper function")
        return func(*args, **kwargs)
        
    return wrapper

@decorator
def sum(a,b):

    return a+b

print(sum(2,4))


@decorator
def mixed(a,b,c,d,e):
    print(a+b+c)
    print(d,e)
