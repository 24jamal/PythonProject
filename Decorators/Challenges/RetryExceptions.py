import logging
import time
import random

# Create a decorator @retry(times=3) that retries 
# a failing function (raises exception) up to 3 times before giving up.

logging.basicConfig(
    level= logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s",
    filename = "Decorators/Challenges/function_logs.txt"
)


def retry(retry= 3, delay =1):
    def decorator(func):
        def wrapper(*args, **kwargs):

            current_attempt = 1
            while current_attempt <= retry:

                try:

                    logging.info("Function Parameters : {args} || Keyword Args :{kwargs}")
                    logging.debug(f"Attempt No : {current_attempt}")
                    return func(*args, **kwargs)
                
                except Exception as e:
                    logging.error(f"Attempt failed no : {current_attempt}")

                    if (current_attempt == retry):

                        logging.error(f"Total Attempts reached : {retry}")
                        raise
                    else:

                        current_attempt = current_attempt +1
                        time.sleep(1)
        return wrapper
    return decorator


@retry(retry=3, delay = 1)
def lucky_draw():

    choice = random.choice([1,2,3,4,5])
    print(f"Choice : {choice}")

    if choice != 5:

        raise ValueError("Better Luck Next Time ")

    return "Hooray! Youre won!!"


try:
    print(lucky_draw())
except Exception as e:
    print("Final failure:", e)