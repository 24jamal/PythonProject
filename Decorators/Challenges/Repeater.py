def decorator(func):

    def wrapper(*args, **kwargs):

        print("Inside wrapper")


        count =0
        mylist = []
        for i in range(1,4):
            print(f"Execution no : {i}")
            a = func(*args)
            mylist.append(a)
            count = count +1
        
        print(f"Total Executions {count}")
        
        print("end of wrapper")

        return mylist

    return wrapper

@decorator
def sum(a,b,c,d):
    return a+b+c+d

print(sum(2,3,4,5))