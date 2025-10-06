def myfunc(**kwargs):

    if 'food' in kwargs:

        print(kwargs['food'])


myfunc(bag= "lenovo",laptop="HP",food="rice")

#Example with *agrs and **args

def myfunc2(*args, **kwargs):

    print(args)
    print(kwargs)
    print(args[0], kwargs['bike'])


myfunc2(2,3,4,5,5,6,lunch = "Rice",bike = "Activa",cloth = "Otto")