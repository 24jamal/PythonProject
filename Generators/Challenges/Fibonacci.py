def fibonacci(n):

    a= 0
    b =1
    count = 0
    while count <= n:

        yield a
        a, b = b , a+b
        count = count +1

for i in fibonacci(10):
    print(i)