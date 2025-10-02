# List Comprehension : [expression for item in iterable if condition]

a = [1,2,3,4,5,6,7]

#without if condition
b = [x**2 for x in a ]

#With if condition
c = [x**2 for x in a if x%2 ==0]


#if-else

d = ["even" if x %2 == 0 else "odd" for x in a]


print(b)
print(c)
print(d)



#using functions in list comprehension
def isPrime(num):

    for i in range(2, num//2 +1):

        if (num %2 == 0):
            print(f"{num} is not Prime Number")
            return False
    
    print(f"{num} is a Prime Number")
    return True

checkforprimes = [10,3,4,56,22,7,43]
primes = [isPrime(x) for x in checkforprimes]
print(primes)

# String Manipulation
sentence = "one two three four"
words = sentence.split()

Upperwords = [w.upper() for w in words]

print(Upperwords)


#Nested Loops in Comprehension

pairs = [(x,y) for x in [1,2] for y in [3,4]]
print(pairs)

#Flatten a Matrix

matrix = [[1,2],[3,4],[5,6]]

flat = [num for row in matrix for num in row]
print(f"flat is {flat}")