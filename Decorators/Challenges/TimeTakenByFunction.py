import time
import logging

logging.basicConfig(
    level= logging.DEBUG,
    format= "%(asctime)s %(levelname)s  %(message)s",
    filename= "Decorators/Challenges/function_logs.txt"

)

def time_taken_decorator(func):

    def wrapper(*args, **kwargs):

        logging.debug("----------------------------")
        print("Inside Wrapper")
        logging.debug("Inside Wrapper function")
        start = time.perf_counter()
        result =  func(*args, **kwargs)
        end = time.perf_counter()
        time_taken = (end - start)
        logging.info(f"Execution time of {func.__name__} is : {time_taken:.4f}")
        logging.info(f"Arguments : {args} || Key word Arguments : {kwargs}")
        print(f"{time_taken:.4f} seconds")
        logging.info("End of wrapper")
        return result
    
    logging.warning("End of time_taken_decorator() function")
    return wrapper


@time_taken_decorator
def justloop():
    total = 0
    for i in range(101):

        total = total + i
        time.sleep(0.1)
    return total

print(justloop())