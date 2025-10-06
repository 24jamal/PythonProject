def square_or_cube(num):

    if num % 2 == 0:
        return num * num
    
    else:
        return num * num * num
    

square_or_cube_lambda = lambda num : num ** 2 if num % 2 == 0 else num ** 3

#Lambda function -> funcname = lamdba inputs : output if condition else condition
print(square_or_cube(3))
print(square_or_cube(4))

print(square_or_cube_lambda(3))
print(square_or_cube_lambda(4))