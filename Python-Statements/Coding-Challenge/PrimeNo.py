def isPrime(num):

    print(num//2 +1)
    for i in range(2, num//2 +1):

        if (num %2 == 0):
            print(f"{num} is not Prime Number")
            return False
    
    print(f"{num} is a Prime Number")
    return True

isPrime(19)