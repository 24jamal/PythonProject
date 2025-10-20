def dividetheNumber():
    a = 10
    b = 0
    try :

        c = a/b
        print(c)
    except ZeroDivisionError as e:
        print("Custom error Handling : Number cant be divided by Zero")
        raise

def main():

    try :
        dividetheNumber()
    except ZeroDivisionError as e:
        print(e)

main()