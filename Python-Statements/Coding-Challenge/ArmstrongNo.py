num = 371
temp =num
remainder = 1
result =0

while(temp >0):

    remainder = temp %10
    result = result + (remainder * remainder *remainder)
    temp = temp//10

if (num == result):
    print(f"{result} is Armstrong Number")
else:
    print(f"{result} is not Armstring number")