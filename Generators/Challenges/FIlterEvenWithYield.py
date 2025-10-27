def square(gen):

    for num in gen:
        yield num**2


def filter_even(gen):

    for num in gen:
        if num %2 == 0:
            yield num

def gen_numbers(n):

    count = 1

    while count < n:

        yield count
        count = count +1 


result = square(filter_even(gen_numbers(10)))

for i in result :
    print(i)