import logging

logging.basicConfig(

    filename = "logging_error.txt",
    level= logging.ERROR,
    format= "%(asctime)s  %(levelname)s %(message)s"
)

try :
    a=10
    b = 0
    c = a/b

except ZeroDivisionError as e:
    logging.exception(e)


