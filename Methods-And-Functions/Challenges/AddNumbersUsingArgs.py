def myfunc(*args):

    total = 0
    for i in args:

        print(i)
        total = total + i

    print(total)


myfunc(2,2,4,5,5)
