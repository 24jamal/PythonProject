import threading

def count():
    x = 0
    for i in range(10_000_000):
        x += 1

t1 = threading.Thread(target=count)
t2 = threading.Thread(target=count)

t1.start()
t2.start()

t1.join()
t2.join()