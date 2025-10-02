#Logical Operators (not, or, and)

age = 18
hasId = True

if ((age >= 18) and (hasId)):
    print("You can vote")

if ((age <= 18) and not(hasId == True)):
    print("Youre not eligible to vote")


meena = 0
teena = 0

if (meena == 1 or teena == 1):
    print("Both of them allowed")

else:
    print("Both of them not Allowed ")


print(not(True))