def read_and_calculate(filename):

    try :
        file = open(filename,"r")

        data = file.read().strip()

        print(data)
    
        try:
            
            num = float(data)

            result = 100 / num
            print(f"result : {result}")

        except ValueError as e:
            print(e)

        except ZeroDivisionError as e:
            print(e)
    
    except FileNotFoundError as e:
        print(e)

    except PermissionError as e :
        print(e)
    

read_and_calculate("ErrorAndExceptionsHandling/Challenges/data.txt")
