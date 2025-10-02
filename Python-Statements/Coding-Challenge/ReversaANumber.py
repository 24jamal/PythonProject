num = 123
temp = num
reverseno = 0

print(f"temp is {temp}")
while (temp > 0):

    digit = (temp %10)

    reverseno = (reverseno*10) + digit

    temp = temp // 10

    print(f"temp in fuction {reverseno}")

print(reverseno)

    
