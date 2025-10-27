import time
def generator(n):

    count =1
    print(f"Inside Count : {count} ")
    while count < n:

        print(f"While Count : {count} ")
        yield count

        count = count +1 

start = time.perf_counter()
for i in generator(10):
    
    print(i)

end = time.perf_counter()

result = f"{end - start:.2f}"
print(result)