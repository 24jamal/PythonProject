# 3 ->Fizz
# 5 ->Buzz
# 3 & 5 -> FizzBuzz

num = 20

for i in range(1,num+1):
    if (i %3 ==0 and i %5 ==0):
        print(f"{i} is FizzBuzz")
    elif (i %3 == 0):
        print(f"{i} is Fizz")
    elif (i % 5 == 0) :
        print(f"{i} is Buzz")