from multiprocessing import Process
import time

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")

p1 = Process(target=task, args=("Task1",))
p2 = Process(target=task, args=("Task2",))

p1.start()
p2.start()

p1.join()
p2.join()