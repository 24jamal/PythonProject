#one.py


def my_func():
    print("Hello World")

print("One file is executed")

def my_fun2():
    print("Hello Fish")

def my_fun3():
    print("Hello Elephant")
if __name__ == "__main__":
    print("One file was ran directly")
    my_fun3()
    my_fun2()
    
else:
    print("One file was imported")
