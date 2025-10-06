#check divisibility

def check_divisibility(num):

    if num % 3 ==0 and num % 5 == 0:
        print("SUCCESS")

    else:
        print("FAILED")


check_divisibility_lambda = lambda num : print("SUCCESS") if num % 3 == 0 and num % 5 == 0 else print("FAILED")
check_divisibility(20)

check_divisibility_lambda(20)