try :

    a = int(input("Enter a number1 :"))
    b = int(input("Enter a number2 :"))

    c = a/b
    print(c)

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)