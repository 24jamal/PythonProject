"""
==, != → equality

>, <, >=, <= → numeric comparison

is, is not → object identity

in, not in → membership

"""

a = 10
b = 20

if (a == b):
    print(f"{a} is equal to {b}")

if (a != b):
    print(f"{a} is not equal to {b}")

x = 34
y = 55
if (x > y):
    print(f"{x} is greater than {y}")

if (x < y):
    print(f"{x} is lesser than {y}")


age = int(input("Enter your age"))
if (age >= 18):
    print("Youre eligible to vote")

else :
    print("Youre not eligible")