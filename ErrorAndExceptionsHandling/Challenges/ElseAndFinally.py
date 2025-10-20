def filereader(filename):

    try: 
        file = open(filename,"r")
        print(file.read())
    
    except FileNotFoundError as e:
        print(e)
    
    except FileExistsError as e:
        print(e)
    else :
        print("File was successfully read")
    
    finally:
       # file.close()
        print("File closed and finally ran successfully")

filereader("ErrorAndExceptionsHandling/Challenges/data.txt")