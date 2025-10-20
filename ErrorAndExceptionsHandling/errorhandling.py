def divide(a,b):

    try : 
        c = a/b
    except ZeroDivisionError:

        print("Number cant be divide by zero")

    except TypeError:
        print("Please give as numbers")
    else:
        print(f"{c}")
    
    finally:
        print("I always print")

divide(4,2)
divide(3,0)

divide(3,'2')