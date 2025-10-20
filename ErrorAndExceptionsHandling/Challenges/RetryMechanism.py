import random
import time

def divide_num():


   
    for attempt in range(0,4):
        a = random.randint(1,20)
        b = random.randint(0,5)

        try : 
            c = a/b
            print(c)
            time.sleep(1)

        except ZeroDivisionError as e:
            print(e)
            time.sleep(1)


divide_num()