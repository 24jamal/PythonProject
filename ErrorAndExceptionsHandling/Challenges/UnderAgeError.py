class UnderAgeError(Exception):

    pass


try :
    age = int(input("Enter the age"))

    if age < 18:

        raise UnderAgeError("Youre underage")
    
    else:
        print("Access Granted")

except UnderAgeError as e:
    print(e)