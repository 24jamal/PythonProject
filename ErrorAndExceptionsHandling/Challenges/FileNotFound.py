try :

    file = open("ErrorAndExceptionsHandling/Challenges/data.txt",'r')
    print(file.read())

except FileNotFoundError as e:
    print(e)