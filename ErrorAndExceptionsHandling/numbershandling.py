def add(a,b):

    try : 
        c = a+b
        print(c)
    except:
        print("Please give in number format")
    finally:
        print("I always print")

add(3,'3')
add(5,6)