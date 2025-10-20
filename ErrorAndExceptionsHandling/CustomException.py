class UserAgeError(Exception):
    pass


try :
    age = int(input("Enter the age"))

    if age < 18:
        raise UserAgeError("Youre underage")

except UserAgeError as e:
    print(e)