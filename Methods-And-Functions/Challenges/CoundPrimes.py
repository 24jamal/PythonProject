def isPrime(num):

    #print(num//2 +1)
    for i in range(2, num//2 +1):

        if (num %i == 0):
            #print(f"{num} is not Prime Number")
            return False
    
    #print(f"{num} is a Prime Number")
    return True

def countprimes(num):

    primecount = 0
    for i in range(2,num+1):

        if isPrime(i):
            print(f"{i} is Prime Number")
            primecount = primecount +1
        else:
            print(f"{i} is not a Prime Number")
        
    
    print(f"Total prime numbers in {num} is {primecount}")


countprimes(100)