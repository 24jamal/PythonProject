def hello_with_kwargs(**kwargs):


    if kwargs == None:

        print("hello guest")
        return


    for key, value in kwargs.items():

        print(f"Hello {value}")


#hello_with_kwargs(guest = "Jamal",guest2 = "kamal", guest3= "Kate",guest4 = "Ana")

hello_with_kwargs()