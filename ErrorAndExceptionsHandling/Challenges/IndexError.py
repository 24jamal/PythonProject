mylist = ["Apple","Orange","Pears","Grapes"]

try :
    index = int(input("Enter the index :: "))

    print(mylist[index])

except IndexError as e:
    print(e)