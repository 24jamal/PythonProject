def primeno(gen):

    for i in gen:

        div = int((i +1) /2)
        j = 2
        for j in range(1,div,1):
            if i %j != 0:
                yield i

def numgen(n):

    count = 1

    while count < n:

        yield count 
        count = count +1

result = primeno(numgen(10))

for i in result:
    print(i)