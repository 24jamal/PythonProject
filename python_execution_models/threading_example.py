import threading
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

t1 = threading.Thread(target=task, args=("Task1",))
t2 = threading.Thread(target=task, args=("Task2",))

t1.start()
t2.start()

t1.join()
t2.join()